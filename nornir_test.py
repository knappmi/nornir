# Perform the required imports
from helpers import nornir_setup
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file

# Perform the Nornir initialization
nr = nornir_setup()

# Set the path to where we want the backups to be saved
BACKUP_PATH = "./data/configs"

# Create a Nornir Task.
def backup_config(task, path):
    # Task 1. Run the NAPALM config getter to collect the config
    device_config = task.run(task=napalm_get, getters=["get_config"])

    # Task 2. Write the device config to a file using the Nornir, write_file task
    task.run(
        task=write_file,
        content=device_config.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )

# Run our back_config task against all of our devices. We provide the backup path and also the task name we want to run against all the devices.
result = nr.run(
    name="Backup Device configurations", path=BACKUP_PATH, task=backup_config
)

# Finally, we print the results of running our task against all the devices.
print_result(result, vars=["stdout"])