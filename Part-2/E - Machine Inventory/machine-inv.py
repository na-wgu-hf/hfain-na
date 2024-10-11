import configparser

config = configparser.ConfigParser()

machines = {
    'WindowsDesktop-1': '10.10.1.35',
    'WindowsDesktop-2': '10.10.1.36',
    'WindowsDesktop-3': '10.10.1.43',
    'WindowsDesktop-4': '10.10.1.29',
    'Test_Box_1': '10.10.1.56',
    'Test_Box_2': '10.10.1.57',
}

mac_addresses = {
    'WindowsDesktop-1': '0c:4b:3c:0a:00:00',
    'WindowsDesktop-2': '0c:59:fd:86:00:00',
    'WindowsDesktop-3': '0c:e2:07:f3:00:00',
    'WindowsDesktop-4': '0c:46:74:35:00:00',
    'Test_Box_1': '0c:cb:a8:90:00:00',
    'Test_Box_2': '0c:50:a2:8a:00:00',
}

# Add General and Network Settings for each switch
for machine_name, machine_ip in machines.items():
# General Settings section
    config.add_section(f'{machine_name}_General_Settings')
    config.set(f'{machine_name}_General_Settings', 'Name', machine_name)
    config.set(f'{machine_name}_General_Settings', 'IP_Address', machine_ip)
    config.set(f'{machine_name}_General_Settings', 'RAM', '4096MB')
    config.set(f'{machine_name}_General_Settings', 'vCPUs', '2')
    config.set(f'{machine_name}_General_Settings', 'QEMU_binary', '/bin/qemu-system-x86_64(v4.2.1)')
    config.set(f'{machine_name}_General_Settings', 'Boot_Priority', 'HDD')
    config.set(f'{machine_name}_General_Settings', 'On_Close', 'Send the shutdown signal (ACPI)')
    config.set(f'{machine_name}_General_Settings', 'Console_Type', 'vnc')

    # Network Settings section
    config.add_section(f'{machine_name}_Network_Settings')
    config.set(f'{machine_name}_Network_Settings', 'Adapters', '1')
    config.set(f'{machine_name}_Network_Settings', 'Base_MAC', mac_addresses[machine_name])
    config.set(f'{machine_name}_Network_Settings', 'Type', 'Intel Gigabit Ethernet (e1000)')
    config.set(f'{machine_name}_Network_Settings', 'Replicate Network Connection States in Qemu', 'True')

config.add_section('machines')
config.set('machines', 'WindowsDesktop-1', '10.10.1.35')
config.set('machines', 'WindowsDesktop-2', '10.10.1.36')
config.set('machines', 'WindowsDesktop-3', '10.10.1.43')
config.set('machines', 'WindowsDesktop-4', '10.10.1.29')
config.set('machines', 'Test_Box_1', '10.10.1.56')
config.set('machines', 'Test_Box_2', '10.10.1.57')

# Write the configuration to an INI file
with open('access_closet_machineinventory.ini', 'w') as configfile:
    config.write(configfile)