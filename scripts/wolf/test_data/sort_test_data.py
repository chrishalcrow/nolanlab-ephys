
from argparse import ArgumentParser
from pathlib import Path
from nolanlab_ephys.lab_utils import get_recording_folders, chronologize_paths
from nolanlab_ephys.sort import do_sorting_pipeline_concat
from test_data_eddie import recording_paths
import spikeinterface.full as si

def main():

    parser = ArgumentParser()

    parser.add_argument('--data_folder', default=None)
    parser.add_argument('--deriv_folder', default=None)

    deriv_folder = parser.parse_args().deriv_folder
    data_folder = parser.parse_args().data_folder
    
    print(f"\nWill sort the following recordings:")
    for recording_path in recording_paths:
        print(f"  - {recording_path}")

    recordings = [si.read_openephys(recording_path) for recording_path in recording_paths]

    protocol = 'lupinA'

    analyzer_paths = [
        deriv_folder / recording_path.name for recording_path in recording_paths
    ]

    for recording, analyzer_path in zip(recordings, analyzer_paths):
    
        do_sorting_pipeline_concat(
            recording,
            analyzer_path,
            protocol,
            sorting_output_folder=f"sorting_output_{analyzer_path.name}",
            n_jobs=8,
        )


if __name__ == "__main__":
    main()
