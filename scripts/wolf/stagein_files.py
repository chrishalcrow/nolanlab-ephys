from nolanlab_ephys.eddie import filepath_from_mouse_day_sessions, make_and_run_script
from argparse import ArgumentParser
from nolanlab_ephys.common_paths import eddie_active_projects
from nolanlab_ephys.utils import get_recording_folders

parser = ArgumentParser()

parser.add_argument('mouse')
parser.add_argument('day')
parser.add_argument('sessions')
parser.add_argument('destination')

mouse = int(parser.parse_args().mouse)
day = int(parser.parse_args().day)
sessions_string = parser.parse_args().sessions
sessions = sessions_string.split(',')
destination = parser.parse_args().destination

active_projects_path = eddie_active_projects
data_path = active_projects_path / "Harry/EphysNeuropixelData/"

recording_paths = get_recording_folders(data_path, mouse, day)

print(f"Getting recordings {recording_paths}.")

stagein_script_name = f"M{mouse}D{day}_in"
script_name = make_and_run_script(active_projects_path, recording_paths, destination, stagein_script_name)
