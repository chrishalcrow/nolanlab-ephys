import spikeinterface.full as si

import pandas as pd
from nolanlab_ephys.si_protocols import generic_postprocessing
from pathlib import Path
import numpy as np
from argparse import ArgumentParser

data_folder = Path("/exports/eddie/scratch/chalcrow/harry/data/")
deriv_folder = Path("/exports/eddie/scratch/chalcrow/harry/derivatives/")

parser = ArgumentParser()

parser.add_argument('mouse')
parser.add_argument('day')

mouse = int(parser.parse_args().mouse)
day = int(parser.parse_args().day)

all_rec_samples = pd.read_csv("scripts/harry/resources/all_rec_samples_of_vr_of.csv")
samples = all_rec_samples.query(f'mouse == {mouse} & day == {day}')

of1_samples, vr_samples, of2_samples = samples[['of1','vr','of2']].values[0]

print(of1_samples, vr_samples, of2_samples)

si.set_global_job_kwargs(n_jobs=8)

analyzer_path = deriv_folder / f"M{mouse}/D{day}/full/kilosort4/sub-{mouse}_ses-{day}_srt-kilosort4_full_analyzer.zarr"
analyzer = si.load_sorting_analyzer(analyzer_path)

sorting = analyzer.sorting
recording = analyzer.recording

of1_sorting = sorting.frame_slice(start_frame=0, end_frame=of1_samples)
of1_recording = recording.frame_slice(start_frame=0, end_frame=of1_samples)

vr_sorting = sorting.frame_slice(start_frame=of1_samples, end_frame=of1_samples+vr_samples)
vr_recording = recording.frame_slice(start_frame=of1_samples, end_frame=of1_samples+vr_samples)

of2_sorting = sorting.frame_slice(start_frame=of1_samples+vr_samples, end_frame=None)
of2_recording = recording.frame_slice(start_frame=of1_samples+vr_samples, end_frame=None)

sortings = [of1_sorting, vr_sorting, of2_sorting]
recordings = [of1_recording, vr_recording, of2_recording]
typs = ['OF1', 'VR', 'OF2']

for recording, sortings, typ in zip(recordings, sortings, typs):

    # we do all our syncing assuming that t=0 is at the start of the ephys data
    recording._recording_segments[0].t_start = 0

    analyzer = si.create_sorting_analyzer(
        recording=recording,
        sorting=sorting, 
        folder = deriv_folder / f"M{mouse:02d}/D{day:02d}/{typ}/kilosort4/sub-{mouse:02d}_ses-{day:02d}_typ-{typ}_srt-kilosort4_analyzer",
        format = "zarr",
        peak_sign = "both",
        radius_um = 70,
    )

    analyzer.compute(generic_postprocessing)

#recording = get_chrono_concat_recording(data_folder=data_folder, mouse =mouse, day=day)
#recording = si.aggregate_channels(recording.split_by('group'))

# pp_rec = si.common_reference(si.bandpass_filter(recording))

# old_channel_locations = analyzer.get_channel_locations()
# all_channel_locations = recording.get_channel_locations()

# old_channel_ids = []
# for channel_id, channel_locations in zip(recording.get_channel_ids(), recording.get_channel_locations()):
#     if 2 in np.sum(channel_locations == old_channel_locations, axis=1):
#         old_channel_ids.append(channel_id)

# analyzer._recording = pp_rec.select_channels(old_channel_ids)

# from copy import deepcopy
# new_analyzer = analyzer.save_as(format="memory")
# all_extensions = deepcopy(new_analyzer.extensions)
# for extension_name in all_extensions:
#    new_analyzer.delete_extension(extension_name)

# new_analyzer.sorting = si.remove_excess_spikes(new_analyzer.sorting, new_analyzer._recording)

# new_sparsity = si.estimate_sparsity(new_analyzer.sorting, new_analyzer._recording, peak_sign="both", radius_um=70)
# new_analyzer.sparsity = new_sparsity

# new_analyzer.compute({
#     'unit_locations': {},
#     'random_spikes': {},
#     'noise_levels': {},
#     'waveforms': {},
#     'templates': {},
#     'spike_amplitudes': {'peak_sign': 'both'},
#     'isi_histograms': {},
#     'spike_locations': {'spike_retriver_kwargs': {'peak_sign': 'both'}},
#     'correlograms': {},
#     'template_similarity': {'method': 'l2'},
#     'quality_metrics': {'metric_names': ['num_spikes', 'firing_rate', 'presence_ratio', 'snr', 'isi_violation', 'rp_violation', 'sliding_rp_violation', 'amplitude_cutoff', 'amplitude_median', 'amplitude_cv', 'synchrony', 'firing_range', 'drift', 'sd_ratio'], 'metric_params': {'snr': {'peak_sign': 'both'}, 'amplitude_cutoff': {'peak_sign': 'both'}, 'amplitude_median': {'peak_sign': 'both'}}},
#     'template_metrics': {'include_multi_channel_metrics': True, 'peak_sign': 'both'},
# })

# new_analyzer_path = deriv_folder / f"M{mouse}/D{day}/full/kilosort4/sub-{mouse}_ses-{day}_srt-kilosort4_full_analyzer"
# new_analyzer.save_as(folder=new_analyzer_path, format="zarr")