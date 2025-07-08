from argparse import ArgumentParser
from pathlib import Path
from nolanlab_ephys.si_protocols import protocols
from nolanlab_ephys.utils import get_chrono_concat_recording
from nolanlab_ephys.si_protocols import generic_postprocessing

import spikeinterface.full as si

def main():

    parser = ArgumentParser()

    parser.add_argument('mouse')
    parser.add_argument('day')
    parser.add_argument('sessions')
    parser.add_argument('protocols')
    parser.add_argument('--data_folder', default=None)
    parser.add_argument('--deriv_folder', default=None)

    mouse = int(parser.parse_args().mouse)
    day = int(parser.parse_args().day)

    sessions_string = parser.parse_args().sessions
    sessions = sessions_string.split(',')

    protocols = parser.parse_args().protocols
    protocols_list = protocols.split(',')

    data_folder = parser.parse_args().data_folder
    if data_folder is None:
        data_folder = "/home/nolanlab/Work/Harry_Project/data/"
    data_folder = Path(data_folder)

    deriv_folder = parser.parse_args().deriv_folder
    if deriv_folder is None:
        deriv_folder = "/home/nolanlab/Work/Harry_Project/derivatives/"
    deriv_folder = Path(deriv_folder)

    si.set_global_job_kwargs(n_jobs=10)

    for protocol in protocols_list:
        _ = do_sorting_pipeline(mouse, day, sessions, data_folder, deriv_folder, protocol)

def do_sorting_pipeline(mouse, day, sessions, data_folder, deriv_folder, protocol):

    protocol_info = protocols[protocol]

    recording = get_chrono_concat_recording(data_folder=data_folder, mouse=mouse, day=day)

    pp_recording = si.apply_preprocessing_pipeline(recording, protocol_info['preprocessing'])

    sorting = si.run_sorter(recording=pp_recording, **protocol_info['sorting'], remove_existing_folder=True, verbose=True)

    analyzer = si.create_sorting_analyzer(
        recording=si.apply_preprocessing_pipeline(recording, protocol_info['preprocessing_for_analyzer']), 
        sorting=sorting, 
        folder = deriv_folder / f"M{mouse}/D{day}/{''.join(sessions)}/{protocol}/{protocol}_sa",
        format = "binary_folder"
    )

    analyzer.compute(generic_postprocessing)

    si.export_report(sorting_analyzer=analyzer, output_folder=deriv_folder / f"M{mouse}/D{day}/{''.join(sessions)}/{protocol}/{protocol}_report")

    return analyzer

if __name__ == "__main__":
    main()