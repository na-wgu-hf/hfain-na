import configparser

config = configparser.ConfigParser()

switches = {
    'Local_Switch': '10.10.1.24',
    'IT_Network': '10.10.1.30',
    'MGMT_Network': '10.10.1.31',
    'ACCT_Network': '10.10.1.32',
    'User_Network': '10.10.1.22',
}

mac_addresses = {
    'Local_Switch': '0c:c0:5e:66:00:00',
    'IT_Network': '0c:1c:b2:85:00:00',
    'MGMT_Network': '0c:cc:78:5d:00:00',
    'ACCT_Network': '0c:40:34:07:00:00',
    'User_Network': '0c:e0:f2:0b:00:00',
}

# Add General and Network Settings for each switch
for switch_name, switch_ip in switches.items():
# General Settings section
    config.add_section(f'{switch_name}_General_Settings')
    config.set(f'{switch_name}_General_Settings', 'Name', switch_name)
    config.set(f'{switch_name}_General_Settings', 'IP_Address', switch_ip)
    config.set(f'{switch_name}_General_Settings', 'RAM', '512MB')
    config.set(f'{switch_name}_General_Settings', 'vCPUs', '1')
    config.set(f'{switch_name}_General_Settings', 'QEMU_binary', '/usr/bin/qemu-system-x86_64(v4.2.1)')
    config.set(f'{switch_name}_General_Settings', 'Boot_Priority', 'CD/DVD-ROM or HDD')
    config.set(f'{switch_name}_General_Settings', 'On_Close', 'Power off the VM')
    config.set(f'{switch_name}_General_Settings', 'Console_Type', 'telnet')

    # Network Settings section
    config.add_section(f'{switch_name}_Network_Settings')
    config.set(f'{switch_name}_Network_Settings', 'Adapters', '13')
    config.set(f'{switch_name}_Network_Settings', 'Base_MAC', mac_addresses[switch_name])
    config.set(f'{switch_name}_Network_Settings', 'Type', 'Realtek 8139 Ethernet (rtl8139)')
    config.set(f'{switch_name}_Network_Settings', 'Replicate Network Connection States in Qemu', 'True')

config.add_section('Switches')
config.set('Switches', 'Local_Switch', '10.10.1.24')
config.set('Switches', 'IT_Network', '10.10.1.30')
config.set('Switches', 'MGMT_Network', '10.10.1.31')
config.set('Switches', 'ACCT_Network', '10.10.1.32')
config.set('Switches', 'User_Network', '10.10.1.22')

# Write the configuration to an INI file
with open('access_closet_inventory.ini', 'w') as configfile:
    config.write(configfile)