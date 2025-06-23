from datetime import datetime
import numpy.random as random
import pandas as pd
import subprocess

def make_and_run_script(active_projects_path, recording_paths, destination_folder):

    script_text = """# Grid Engine options start with a #$
#$ -N stagein
#$ -cwd
#$ -q staging

# Hard runtime limit
#$ -l h_rt=00:30:00 

"""

    for recording_path in recording_paths:
        script_text += f"cp -rn {active_projects_path + recording_path} {destination_folder}\n"

    filename = 'stagein_{date:%Y-%m-%d_%H:%M:%S}_{rando}.txt'.format( date=datetime.now(), rando= random.randint(100))  

    with open(filename, "w") as f:
        f.write(script_text)

    subprocess.run(['qsub', filename])

def filepath_from_mouse_day_sessions(mouse, day, sessions, path_to_all_filepaths="all_filepaths.csv"):

    all_filepaths = pd.read_csv(path_to_all_filepaths)

    mouseday_filepaths = [all_filepaths.query(f'mouse == {mouse} & day == {day} & session == "{session}"')['filepath'].values[0] for session in sessions]

    return mouseday_filepaths

