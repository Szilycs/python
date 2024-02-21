from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "131.226.217.181",
    "username": "admin",
    "password": "C1sco12345"
}


net_connect = ConnectHandler(**cisco1)
#print(net_connect.find_prompt())
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_config_set("banner motd #szilard#")
    #output += net_connect.save_config()
net_connect.disconnect()
print(output)
