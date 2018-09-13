import sys
import time
from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

connection.enable()

commands=['interface G2', 'description Connects to ASAv', 'ip address 203.0.113.1 255.255.255.192', 'no shut']
connection.config_mode()

connection.send_config_set(config_commands=commands)
time.sleep(2)

interface_output = connection.send_command('show run int G2')
print(interface_output)

interface_status = connection.send_command('show ip int G2 | in GigabitEthernet2')
if interface_status.count('up') == 2:
    print('Interface is up/up. Continue execution')
else:
    print('Something went wrong. Cancel execution')
    sys.exit()

commands=['ip route 10.255.255.2 255.255.255.255 203.0.113.1']

connection.send_config_set(config_commands=commands)
time.sleep(2)

route_output = connection.send_command('show ip route | in 10.255.255.2')
if 'Network not in table' in route_output:
    print('Route not found in table. Cancel execution')
    sys.exit()
else:
    print('Route found in table. Continue execution')

