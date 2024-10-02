import configparser

config = configparser.ConfigParser()

    # Add Group 1: Switches
    config.add_section('Switches')
    config.set('Switches', 'Local_Switch', '10.10.1.2')
    config.set('Switches', 'IT_Network', '10.10.1.5')
    config.set('Switches', 'MGMT_Network', '10.10.1.6')
    config.set('Switches', 'ACCT_Network', '10.10.1.7')
    config.set('Switches', 'User_Network', '10.10.1.8')

    # Add Group 2: Windows machines
    config.add_section('Windows_Machines')
    config.set('Windows_Machines', 'WD-1', '10.10.1.35')
    config.set('Windows_Machines', 'WD-2', '10.10.1.36')
    config.set('Windows_Machines', 'WD-3', '10.10.1.43')
    config.set('Windows_Machines', 'WD-4', '10.10.1.29')
    config.set('Windows_Machines', 'DC', '10.10.1.28')

    # Add Group 3: Linux machines
    config.add_section('Linux_Machines')
    config.set('Linux_Machines', 'linux_1', '10.10.1.56')
    config.set('Linux_Machines', 'linux_2', '10.10.1.57')

    # Write to grouped_inventory.ini
    with open('grouped_inventory.ini', 'w') as configfile:
        config.write(configfile)