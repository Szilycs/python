import ncclient
from ncclient import manager

payload = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <ipv4/>
      <ipv4-subnet-mask/>
    </interface>
  </interfaces>
</filter>
"""

h = "172.17.255.122"
with manager.connect (host = h, port="830", timeout=None, username="admin", password="admin", hostkey_verify=False) as m:
	request = m.get(payload).xml
	print(request)
