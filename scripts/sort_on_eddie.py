from eddie_helper.make_scripts import run_python_script
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('python_arg')
python_arg = parser.parse_args().python_arg

run_python_script(python_arg, cores=8, email="chalcrow@ed.ac.uk", staging=False)