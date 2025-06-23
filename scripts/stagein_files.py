from nolanlab_ephys.eddie import filepath_from_mouse_day_sessions, make_and_run_script
from argparse import ArgumentParser

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

recording_paths = filepath_from_mouse_day_sessions(mouse, day, sessions)

active_projects_path = "/run/user/1000/gvfs/smb-share:server=cmvm.datastore.ed.ac.uk,share=cmvm/sbms/groups/CDBS_SIDB_storage/NolanLab/ActiveProjects/"

make_and_run_script(active_projects_path, recording_paths, destination)
