import os
from pathlib import Path
from dotenv import load_dotenv
from nornir import InitNornir
from nornir.core import Nornir
from nornir.core.filter import F
from operator import and_, or_
from functools import reduce
from pprint import pprint as pp

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

def filterQuery(nr: Nornir, query_string:str):
    filters = []

    for term in query_string.split('&'):
        negate = True if term.startswith('!') else False

        values = term[1:].split(',') if negate else term.split(',')
        sub_filters = []
        for val in values:
            f_object = ~F(groups__contains=val) if negate else F(groups__contains=val)
            sub_filters.append(f_object)
        
        ord_f_object = reduce(or_, sub_filters)
        filters.append(ord_f_object)
    
    return nr.filter(reduce(and_, filters))