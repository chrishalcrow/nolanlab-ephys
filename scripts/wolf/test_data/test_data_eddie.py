from eddie_helper.make_scripts import run_python_script, run_stage_script
from argparse import ArgumentParser
from pathlib import Path
from common_paths import  eddie_active_projects, eddie_wolf_data_folder, eddie_wolf_deriv_folder
import os
import pandas as pd
    
parser = ArgumentParser()

parser.add_argument('--data_folder', default=None)
parser.add_argument('--deriv_folder', default=None)

deriv_folder = parser.parse_args().deriv_folder
deriv_folder = Path(deriv_folder)

data_folder = parser.parse_args().data_folder
data_folder = Path(data_folder)

active_projects_path = eddie_active_projects
test_folder = active_projects_path / "Wolf/mmnav/data/test"

folder_names = [
    "M3_2025-11-11_15-14-58_S1_test",
]

recording_paths = [
    test_folder / folder_name for folder_name in folder_names
]

stagein_dict = {}
for recording_path in recording_paths:
    recording_folder_name = Path(recording_path).name
    session_type_folder = data_folder
    stagein_dict[f"{active_projects_path / recording_path}"] = session_type_folder / recording_folder_name
    session_type_folder.mkdir(exist_ok=True)

stagein_job_name = f"test_in" 
run_python_name = f"test_run"

uv_directory = os.getcwd()
python_arg = f"scripts/wolf/test_data/sort_test_data.py --data_folder={data_folder} --deriv_folder={deriv_folder}"

email = "chalcrow@ed.ac.uk"

run_stage_script(stagein_dict, job_name=stagein_job_name)
run_python_script(uv_directory, python_arg, cores=8, email=email, staging=False, hold_jid=stagein_job_name, job_name=run_python_name)
