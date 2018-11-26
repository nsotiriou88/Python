import time
import socket
from zeroconf import ServiceBrowser, Zeroconf


class MyListenerForMaster:

    def remove_service(self, zeroconf, service_type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, service_type, name):
        global masterID, masterIP
        info = zeroconf.get_service_info(service_type, name)
        if "Primary" in name:
            masterID = name[9:13]
            masterIP = socket.inet_ntoa(info.address)


zeroconf = Zeroconf()
listener = MyListenerForMaster()
masterID = ''
masterIP = ''

ServiceBrowser(zeroconf, "_svc_openrtls._tcp.local.", listener)

time.sleep(0.5)
if masterID != '' or masterIP != '':
    if masterID[0] == '0':
        masterID = "0x" + masterID[1:]
    else:
        masterID = "0x" + masterID
    print(masterID, masterIP)
else:
    print("No Master Detected")
zeroconf.close()
