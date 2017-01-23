import telnetlib
HOST = "marquise-pc" #ip address or domain
tn =telnetlib.Telnet(HOST,999)

tn.write("Hello World\n")
print(tn.read_all())
