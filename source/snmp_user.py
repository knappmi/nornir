from webbrowser import get
from helpers import nornir_setup
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir.core.exceptions import NornirExecutionError
from nornir.core.task import Task, Result

nr = nornir_setup()
BACKUP_PATH = "./data/snmpConfigs"

def getSnmpUser(task, path):

    backupSnmpConfig = task.run(task=napalm_cli, commands=['show snmp user'])

    task.run(
        task=write_file,
        content=backupSnmpConfig.result['show snmp user'],
        filename=f"{path}/{task.host}.txt"

    )



devicefilter = nr.filter(name='CSR1000V-JCU-TEST3')
result = devicefilter.run(name='SNMP User Runbook Start', task=getSnmpUser, path=BACKUP_PATH)

print_result(result)
print(f'Failed hosts= {result.failed_hosts.keys()}')
