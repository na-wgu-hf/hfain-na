import paramiko
import pandas as pd
import datetime

# Device details (customize these)
devices = [
    {"name": "TestBox1", "ip": "10.10.1.2"}
]

# Function to retrieve settings
def get_device_settings(ip):
    settings = {}
    try:
        # Establish SSH connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username='your_username', password='your_password')  # Update with your credentials
        
        # Sample commands to retrieve settings (customize these according to your environment)
        commands = {
            "General Settings": [
                "echo 'Name: $(hostname)'",
                "echo 'RAM: $(free -h | grep Mem | awk '{print $2}')'",
                "echo 'vCPUs: $(nproc)'",
                "echo 'QEMU binary: $(which qemu-system-x86_64)'",
                "echo 'Boot Priority: <your_command>'",
                "echo 'On close: <your_command>'",
                "echo 'Console type: <your_command>'",
            ],
            "Network Settings": [
                "ip a",
                "echo 'Adapters: <your_command>'",
                "echo 'Base MAC: <your_command>'",
                "echo 'Type: <your_command>'",
                "echo 'Replicate network connection states in QEMU: <your_command>'",
            ]
        }

        for section, cmds in commands.items():
            settings[section] = {}
            for cmd in cmds:
                stdin, stdout, stderr = client.exec_command(cmd)
                output = stdout.read().decode().strip()
                settings[section][cmd] = output
        
        client.close()
    except Exception as e:
        print(f"Error connecting to {ip}: {e}")
    return settings

# Collect data
inventory = []
for device in devices:
    device_settings = get_device_settings(device["ip"])
    inventory.append({"Device": device["name"], "Settings": device_settings})

# Convert to DataFrame and save to CSV
df = pd.DataFrame(inventory)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_csv(f'inventory_{timestamp}.csv', index=False)

print(f"Inventory saved to inventory_{timestamp}.csv")