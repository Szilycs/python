import ncclient
from ncclinet import manager 

hostIP = "devnetconfboxiosxe.cisco.com"
with mannager.connect (host = hostIP, port ="830", timeout=None, username="admin", password="C1sco12345", hostkeyverify=False) as m:
	request=m.get-config(source="running").data_xml()
