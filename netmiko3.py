from netmiko import ConnectHandler
from getpass import getpass
úű
linux = {
    "device_type": "linux",
    "host": "172.19.255.147",
    "username": "szilard",
    "password": getpass()
}


net_connect = ConnectHandler(**cisco1)
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command("show ip ssh")
net_connect.disconnect()
print(output)
