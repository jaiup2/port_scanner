#!/usr/bin/python3
import socket
import sys
import struct
host = sys.argv[1:]
a=[]
def ips(start, end):
	start = struct.unpack('>I', socket.inet_aton(start))[0]
	end = struct.unpack('>I', socket.inet_aton(end))[0]
	for i in range(start, end):
#		print(i)
		host =(socket.inet_ntoa(struct.pack('>I', i)))
		a.append(host)
		host = a
		print(host)
		print(a)
#ips('192.168.74.1', '192.168.74.5')

host1 = ("".join(host[0]))
host1 = host1.split("-")
print(host)
print(host1)
try:
	host[1]
	print("Available")
except Exception:
	print("Not Available")
	host = host1
	try:
		host[1]
		ips(host[0],'192.168.93.140')
	except Exception:
		pass
print("working")
print(host)

#name=socket.gethostbyname("{}".format(host))
#for k in host:
#	print(k)
for j in host:
	print("\n")
	for k in range(1,5):
		try:
			s = socket.socket()
			(s.connect((j, k)))
			print(k,"Port is open for {}".format(j))
		except socket.error as a:
			print(k,"Port is closed for",j)
			pass
