from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
                      'ip': '10.0.0.5',
                      'username': 'ignw',
                      'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

connection.enable()

conf_lo0=['interface Lo0', 'description I made this with Python', 'ip address 172.16.1.1 255.255.255.255']
connection.send_config_set(config_commands=conf_lo0)

interface_output = connection.send_command('show run int Lo0')
print(interface_output)

interface_status = connection.send_command('show int Lo0')
print(interface_status)
