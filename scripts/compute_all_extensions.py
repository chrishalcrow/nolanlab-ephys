import spikeinterface.full as si

from nolanlab_ephys.utils import get_chrono_concat_recording
from pathlib import Path

from argparse import ArgumentParser

data_folder = Path("/exports/eddie/scratch/chalcrow/harry/data/")
deriv_folder = Path("/exports/eddie/scratch/chalcrow/harry/derivatives/")

parser = ArgumentParser()

parser.add_argument('mouse')
parser.add_argument('day')

mouse = int(parser.parse_args().mouse)
day = int(parser.parse_args().day)

si.set_global_job_kwargs(n_jobs=8)

analyzer_path = deriv_folder / f"M{mouse}/D{day}/full/kilosort4/kilosort4_sa"
analyzer = si.load_sorting_analyzer(analyzer_path)

if analyzer.has_extension("spike_locations") is True:
    print(f"skipped M{mouse}_D{day}.")
    exit()

recording = get_chrono_concat_recording(data_folder=data_folder, mouse =mouse, day=day)
pp_rec = si.common_reference(si.bandpass_filter(recording))

if analyzer.get_num_channels() <= 384:
    removed_channels_rec = si.detect_and_remove_bad_channels(pp_rec)
    analyzer._recording = removed_channels_rec
else:
    analyzer._recording = pp_rec

from copy import deepcopy
new_analyzer = analyzer.save_as(format="memory")
all_extensions = deepcopy(new_analyzer.extensions)
for extension_name in all_extensions:
   new_analyzer.delete_extension(extension_name)

new_sparsity = si.estimate_sparsity(new_analyzer.sorting, new_analyzer._recording, peak_sign="both", radius_um=58)
new_analyzer.sparsity = new_sparsity

new_analyzer.compute({
    'unit_locations': {},
    'random_spikes': {},
    'noise_levels': {},
    'waveforms': {},
    'templates': {},
    'spike_amplitudes': {},
    'isi_histograms': {},
    'spike_locations': {},
    'correlograms': {},
    'quality_metrics': {},
    'template_metrics': {'include_multi_channel_metrics': True},
})

new_analyzer_path = deriv_folder / f"M{mouse}/D{day}/full/kilosort4/sub-{mouse}_ses-{day}_full_analyzer"
new_analyzer.save_as(folder=new_analyzer_path, format="zarr")