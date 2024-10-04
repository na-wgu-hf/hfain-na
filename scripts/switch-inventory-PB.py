import configparser

config = configparser.ConfigParser()

switches = {
    'Local_Switch': '10.10.1.24',
    'IT_Network': '10.10.1.30',
    'MGMT_Network': '10.10.1.31',
    'ACCT_Network': '10.10.1.32',
    'User_Network': '10.10.1.22',
}

# Add General and Network Settings for each switch
for switch_name, switch_ip in switches.items():
# General Settings section
    config.add_section(f'{switch_name}_General_Settings')
    config.set(f'{switch_name}_General_Settings', 'Name', switch_name)
    config.set(f'{switch_name}_General_Settings', 'IP_Address', switch_ip)
    config.set(f'{switch_name}_General_Settings', 'RAM', '4GB')  # Placeholder value
    config.set(f'{switch_name}_General_Settings', 'vCPUs', '2')  # Placeholder value
    config.set(f'{switch_name}_General_Settings', 'QEMU_binary', '/usr/bin/qemu-system-x86_64')
    config.set(f'{switch_name}_General_Settings', 'Boot_Priority', 'Disk')
    config.set(f'{switch_name}_General_Settings', 'On_Close', 'Shutdown')
    config.set(f'{switch_name}_General_Settings', 'Console_Type', 'VNC')

    # Network Settings section
    config.add_section(f'{switch_name}_Network_Settings')
    config.set(f'{switch_name}_Network_Settings', 'Adapters', '4')  # Placeholder value
    config.set(f'{switch_name}_Network_Settings', 'Base_MAC', '00:11:22:33:44:55')  # Placeholder value
    config.set(f'{switch_name}_Network_Settings', 'Type', 'virtio')  # Placeholder value
    config.set(f'{switch_name}_Network_Settings', 'Replicate_Network_Connection_States', 'True')

config.add_section('Switches')
config.set('Switches', 'Local_Switch', '10.10.1.24')
config.set('Switches', 'IT_Network', '10.10.1.30')
config.set('Switches', 'MGMT_Network', '10.10.1.31')
config.set('Switches', 'ACCT_Network', '10.10.1.32')
config.set('Switches', 'User_Network', '10.10.1.22')

# Write the configuration to an INI file
with open('access_closet_inventory.ini', 'w') as configfile:
    config.write(configfile)