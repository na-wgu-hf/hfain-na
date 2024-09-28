from netmiko import ConnectHandler

exos_switch = {
    'device_type': 'extreme_exos',
    'host': '10.10.1.1',
    'username': 'admin',
    'password': '',
}

net_connect = ConnectHandler(**exos_switch)
output = net_connect.send_command('show version')
output += net_connect.send_command('show configuration')
output += net_connect.send_command('show vlan')

with open("switch_inventory.txt", "w") as file:
    file.write(output)

print(output)