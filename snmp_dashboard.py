
from pysnmp.entity.rfc3413.oneliner import cmdgen
import re


c1 = 'public'
c2='public'
c3 = 'public'
#myuser='me_srgo6857'
#auth='ngdb@1234'
#priv='ngdb@1234'

host1='198.51.100.3'
host2='198.51.100.4'
host3='198.51.100.5'
port = 161

oids = ['1.3.6.1.2.1.1.4.0',
    '1.3.6.1.2.1.1.5.0',
    '1.3.6.1.2.1.1.6.0',
    '1.3.6.1.2.1.2.1.0',
    '1.3.6.1.2.1.1.3.0']
cmdGen = cmdgen.CommandGenerator()


errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
cmdgen.CommunityData(c1),
cmdgen.UdpTransportTarget((host1, port)),
*oids
)
if errorIndication:
    print(errorIndication)
else:
    print ("*********The Dashboard Displaying the OID's Information in SNMPv1, SNMPv2, SNMPv3********************")
    print ("Author: Srivaishnavi G")
    print ("MS in Network Engineering, CU Boulder")
    print("")
    print("SNMP V1")
    for name, val in varBinds:
            output = ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            output = re.sub(r'^.{12}','',output)
            output = re.sub(r"mib-2.2.1.0", "Number", output)
            print(output)


errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
cmdgen.CommunityData(c2),
cmdgen.UdpTransportTarget((host2, port)),
*oids
)
if errorIndication:
    print(errorIndication)
else:
    print("")
    print("SNMP V2")
    for name, val in varBinds:
            output = ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            output = re.sub(r'^.{12}','',output)
            output = re.sub(r"mib-2.2.1.0", "Number", output)
            print(output)


errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
cmdgen.CommunityData(c3),
cmdgen.UdpTransportTarget((host3, port)),
*oids
)
if errorIndication:
    print(errorIndication)
else:
    print("")
    print("SNMP V3")
    for name, val in varBinds:
            output = ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            output = re.sub(r'^.{12}','',output)
            output = re.sub(r"mib-2.2.1.0", "Number", output)
            print(output)