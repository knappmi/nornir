import os
from pathlib import Path
from dotenv import load_dotenv
from nornir import InitNornir

# Load and populate the environment variables from .env
load_dotenv()

# Set the path to the Nornir config file
NORNIR_CONFIG_FILE = f"{Path(__file__).parent.parent.parent}\\nornir\\nr-config.yml"

# Create a Nornir setup function
def nornir_setup():
    # Initialize Nornir
    nr = InitNornir(config_file=NORNIR_CONFIG_FILE)

    # Set the username and password using the environment variables
    nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
    nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")

    return nr