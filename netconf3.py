import ncclient
from ncclient import manager 

hostIP = "172.17.255.122"
with mannager.connect (host = hostIP, port ="830", timeout=None, username="admin", password="admin", hostkeyverify=False) as m:
	request=m.get_config(source = "running").data_xml
	with open("catalyst8000.xml","w") as f:
		f.write(request)
