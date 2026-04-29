"""
Sorts the IBL data from
    https://dandiarchive.org/dandiset/000409/0.260309.1324/files?location=sub-UCLA034&page=1
For a variety of sorting protocols.
"""

from pathlib import Path
from nolanlab_ephys.sort import do_sorting_pipeline_concat

import spikeinterface.full as si

def main():

    deriv_folder = Path("/home/nolanlab/Work/components_results/ibl")

    recording_path = "/home/nolanlab/Downloads/sub-UCLA034_ses-3537d970-f515-4786-853f-23de525e110f_desc-raw_ecephys.nwb"
    recordings = [si.read_nwb_recording(recording_path, electrical_series_path='acquisition/ElectricalSeriesProbe00AP')]

    protocols = ['lupinB', 'kilosort4B', 'spykingcircus2B', 'tridesclous2B']

    for protocol in protocols:

        analyzer_path = deriv_folder / f"ibl_{protocol}_analyzer"

        do_sorting_pipeline_concat(
            recordings,
            analyzer_path,
            protocol,
            sorting_output_folder=f"sorting_output_{protocol}",
            n_jobs=8,
        )


if __name__ == "__main__":
    main()
