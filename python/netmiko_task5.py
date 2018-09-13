import sys
import time
from netmiko import ConnectHandler

asav = {'device_type': 'cisco_asa',
        'ip': '10.0.0.8',
        'username': 'ignw',
        'password': 'ignw',
        'secret': 'ignw'}
connection = ConnectHandler(**asav)

connection.enable()

commands=['interface GigabitEthernet0/0',
          'description Connects to CSR',
          'nameif outside',
          'security-level 0',
          'ip address 203.0.113.2 255.255.255.192',
          'no shut']
connection.config_mode()

connection.send_config_set(config_commands=commands)
time.sleep(2)

interface_output = connection.send_command('show run int Gig0/0')
print(interface_output)
time.sleep(2)

interface_status = connection.send_command('show int Gig0/0 | in GigabitEthernet0/0')
if interface_status.count('up') == 2:
    print('Interface is up/up. Continue execution')
else:
    print('Something went wrong. Cancel execution')
    sys.exit()

commands=['interface GigabitEthernet0/1',
          'description Connects to NX-OSv',
          'nameif inside',
          'security-level 100',
          'ip address 10.255.255.1 255.255.255.240',
          'no shut']

connection.send_config_set(config_commands=commands)
time.sleep(2)

interface_output = connection.send_command('show run int Gig0/1')
print(interface_output)
time.sleep(2)

interface_status = connection.send_command('show int Gig0/1 | in GigabitEthernet0/1')
if interface_status.count('up') == 2:
    print('Interface is up/up. Continue execution')
else:
    print('Something went wrong. Cancel execution')
    sys.exit()

commands=['route outside 8.8.4.4 255.255.255.255 203.0.113.0']

connection.send_config_set(config_commands=commands)
time.sleep(2)

route_output = connection.send_command('show route | in 10.255.255.2')
if 'Network not in table' in route_output:
    print('Route not found in table. Cancel execution')
    sys.exit()
else:
    print('Route found in table. Continue execution')

print('Adding access-list')

commands=['access-list outside_in extended permit icmp any any',
          'access-group outside_in in interface outside']

connection.send_config_set(config_commands=commands)
time.sleep(2)

connection.send_command('wr')
print('Config complete')
