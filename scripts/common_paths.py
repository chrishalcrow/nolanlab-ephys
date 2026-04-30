"""
File containing useful paths that you might use in your project.
E.g. where the `ActiveProjects` on different machines such as your laptop, desktop and on EDDIE.
Can be a helpful place to store paths to data and derivative folders.
"""

from pathlib import Path

eddie_active_projects = Path(
    "/exports/cmvm/datastore/sbms/groups/CDBS_SIDB_storage/NolanLab/ActiveProjects/"
)

chris_desktop_active_projects = Path(
    "/run/user/1000/gvfs/smb-share:server=cmvm.datastore.ed.ac.uk,share=cmvm/sbms/groups/CDBS_SIDB_storage/NolanLab/ActiveProjects/"
)
chris_laptop_active_projects = Path(
    "/Volumes/cmvm/sbms/groups/CDBS_SIDB_storage/NolanLab/ActiveProjects"
)

eddie_wolf_data_folder = Path('/exports/eddie/scratch/chalcrow/wolf/raw')
eddie_wolf_deriv_folder = Path('/exports/eddie/scratch/chalcrow/wolf/derivatives')

eddie_harry_data_folder = Path('/exports/eddie/scratch/chalcrow/harry/raw')
eddie_harry_deriv_folder = Path('/exports/eddie/scratch/chalcrow/harry/derivatives')

eddie_bri_data_folder = Path('/exports/eddie/scratch/chalcrow/bri/raw')
eddie_bri_deriv_folder = Path('/exports/eddie/scratch/chalcrow/bri/derivatives')

eddie_junji_data_folder = Path('/exports/eddie/scratch/chalcrow/junji/raw')
eddie_junji_deriv_folder = Path('/exports/eddie/scratch/chalcrow/junji/derivatives')

eddie_teris_data_folder = Path('/exports/eddie/scratch/chalcrow/teris/raw')
eddie_teris_deriv_folder = Path('/exports/eddie/scratch/chalcrow/teris/derivatives')