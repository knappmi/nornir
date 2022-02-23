from helpers import nornir_setup, filterQuery
from nornir_netmiko.tasks import netmiko_save_config, netmiko_send_config
from nornir_utils.plugins.functions import print_result
import ipaddress

nr = nornir_setup()

def buildTunnel(task, ep:str, dest):

    tunnel_config_1 = ['interface tunnel15','description Tunnel test 1',f'ip address {ep} 255.255.255.252', 'no shut','tunnel source g1',f'tunnel destination {dest}', 'exit', 'ip route 10.0.0.0 255.255.255.252 tunnel15', 'router eigrp 10', 'network 10.0.0.0 0.0.0.3']
    cliInput = task.run(netmiko_send_config, config_commands=tunnel_config_1)
    cliSave = task.run(netmiko_save_config)

    return cliInput , cliSave

hostname = input(str('What\'s the hostname of the device? '))
endpoint = input(str('What\'s the local endpoint tunnel IP: '))
destination = input(str('What\'s the tunnel destination of the device?'))
device = nr.filter(name=str(hostname))
result = device.run(name='Build Tunnels', ep=endpoint, dest=destination, task=buildTunnel)
print_result(result)