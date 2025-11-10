from argparse import ArgumentParser
from pathlib import Path
from nolanlab_ephys.eddie import filepath_from_mouse_day_sessions
from nolanlab_ephys.common_paths import  eddie_data_folder, eddie_deriv_folder
from nolanlab_ephys.probe_info import rec_to_simple_probe
from nolanlab_ephys.utils import get_recording_folders, chronologize_paths
import matplotlib.pyplot as plt
import numpy as np

parser = ArgumentParser()

parser.add_argument('mouse')
parser.add_argument('day')
parser.add_argument('--data_folder', default=None)
parser.add_argument('--deriv_folder', default=None)

mouse = int(parser.parse_args().mouse)
day = int(parser.parse_args().day)

data_folder = parser.parse_args().data_folder
if data_folder is None:
    data_folder = eddie_data_folder
data_folder = Path(data_folder)

deriv_folder = parser.parse_args().deriv_folder
if deriv_folder is None:
    deriv_folder = eddie_deriv_folder
deriv_folder = Path(deriv_folder)

sessions = ['VR']

recording_path = get_recording_folders(data_folder=data_folder, mouse =mouse, day=day)[0]

probe_vector_representation = rec_to_simple_probe(recording_path)

matrix_representation = np.reshape(probe_vector_representation, (4,4))

fig, ax = plt.subplots()
ax.imshow(matrix_representation.astype('float'))
ax.set_axis_off()
fig.tight_layout()
fig.savefig(deriv_folder / f"M{mouse}_D{day}_probe_layout.png")

