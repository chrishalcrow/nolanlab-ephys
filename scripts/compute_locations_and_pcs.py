import spikeinterface.full as si

from nolanlab_ephys.utils import get_chrono_concat_recording
from pathlib import Path

active_projects_folder = Path("/run/user/1000/gvfs/smb-share:server=cmvm.datastore.ed.ac.uk,share=cmvm/sbms/groups/CDBS_SIDB_storage/NolanLab/ActiveProjects/")
data_folder = active_projects_folder / "Harry/EphysNeuropixelData/"
deriv_folder = active_projects_folder / "Chris/Cohort12/derivatives/"

si.set_global_job_kwargs(n_jobs=4)

ephys_days = {
#    20: [14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],
#    21: [15,16,17,18,19,20,21,22,23,24,25,26,27,28],
#    22: [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51],
    25: [20,21,22,23,24,25,26,27,28,29,30,31,32],
#    26: [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
#    27: [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
#    28: [16,17,18,19,20,21,22,23,24,25,26,27,28,29],
#    29: [16,17,18,19,20,21,22,23,24,25,26,27,28,29]
}

for mouse, days in ephys_days.items():
   for day in days:
        
        analyzer_path = deriv_folder / f"M{mouse}/D{day}/full/kilosort4/kilosort4_sa"
        analyzer = si.load_sorting_analyzer(analyzer_path)

        if analyzer.has_extension("spike_locations") is True:
            print(f"skipped M{mouse}_D{day}.")
            continue

        recording = get_chrono_concat_recording(data_folder=data_folder, mouse =mouse, day=day)
        pp_rec = si.common_reference(si.bandpass_filter(recording))

        if analyzer.get_num_channels() <= 384:
            removed_channels_rec = si.detect_and_remove_bad_channels(pp_rec)
            analyzer._recording = removed_channels_rec
        else:
            analyzer._recording = pp_rec

        analyzer.compute("spike_locations")

        print(f"Finished M{mouse}_D{day}.")