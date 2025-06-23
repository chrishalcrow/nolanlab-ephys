from nolanlab_ephys.eddie import make_and_run_script
from argparse import ArgumentParser
from nolanlab_ephys.common_paths import chris_linux_active_projects


parser = ArgumentParser()

parser.add_argument('mouse')
parser.add_argument('day')
parser.add_argument('destination')

mouse = int(parser.parse_args().mouse)
day = int(parser.parse_args().day)
destination = parser.parse_args().destination

sa_path = [f"Chris/Cohort12/derivatives/M{mouse}/D{day}/full/kilosort4/kilosort4_sa"]

active_projects_path = chris_linux_active_projects

make_and_run_script(active_projects_path, sa_path, destination)
