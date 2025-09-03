from datetime import datetime
import numpy.random as random
import pandas as pd
import subprocess

def make_and_run_script(active_projects_path, recording_paths, destination_folder, script_name, wait_for=None):

    if wait_for is None:
        wait_for = ""

    script_text = f"""# Grid Engine options start with a #$
#$ -N {script_name}{wait_for}
#$ -cwd
#$ -q staging

# Hard runtime limit
#$ -l h_rt=00:30:00 

"""

    for recording_path in recording_paths:
        script_text += f"cp -rn {active_projects_path / recording_path} {destination_folder}\n"

    filename = 'stagein_{date:%Y-%m-%d_%H:%M:%S}_{rando}.sh'.format( date=datetime.now(), rando= random.randint(100))  

    with open(filename, "w") as f:
        f.write(script_text)

    subprocess.run(['qsub', filename])


def make_and_run_stageout(source_folder, active_projects_path, destination_folder, wait_for=None):

    if wait_for is None:
        wait_for = ""

    script_text = f"""# Grid Engine options start with a #$
#$ -N stageout{wait_for}
#$ -cwd
#$ -q staging

# Hard runtime limit
#$ -l h_rt=00:30:00 

"""

    script_text += f"cp -rn {source_folder} {active_projects_path / destination_folder}\n"

    filename = 'stageout_{date:%Y-%m-%d_%H:%M:%S}_{rando}.sh'.format( date=datetime.now(), rando= random.randint(100))  

    with open(filename, "w") as f:
        f.write(script_text)

    subprocess.run(['qsub', filename])

def filepath_from_mouse_day_sessions(mouse, day, sessions=None, path_to_all_filepaths="all_filepaths.csv"):

    all_filepaths = pd.read_csv(path_to_all_filepaths)
    
    if sessions is not None:
        mouseday_filepaths = [all_filepaths.query(f'mouse == {mouse} & day == {day} & session == "{session}"')['filepath'].values[0] for session in sessions]
    else:
        mouseday_filepaths = all_filepaths.query(f'mouse == {mouse} & day == {day}')['filepath'].values
        
    return mouseday_filepaths





def make_and_run_locations_script(mouse, day, wait_for=None):

    if wait_for is None:
        wait_for = ""

    script_text = f"""# Grid Engine options start with a #$
#$ -N M{mouse}D{day}loc
#$ -pe sharedmem 4 -l rl9=true,h_vmem=30G,h_rt=2:00:00{wait_for}
#$ -cwd

source /etc/profile.d/modules.sh

cd /exports/eddie/scratch/chalcrow/harry/fromgit/nolanlab-ephys

/home/chalcrow/.local/bin/uv run scripts/compute_locations_and_pcs.py {mouse} {day}
"""

    filename = f'locations_{mouse}_{day}.sh'

    with open(filename, "w") as f:
        f.write(script_text)

    subprocess.run(['qsub', filename])
