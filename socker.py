#!/usr/bin/python3
import socket
import sys
host = sys.argv[1:]
print(host)
#name=socket.gethostbyname("{}".format(host))
for k in host:
	print(k)
for j in host:
	print("\n")
	for i in range(1,5):
		try:
			s = socket.socket()
			(s.connect((j, i)))
			print(i,"Port is open for {}".format(j))
		except socket.error as a:
			print(i,"Port is closed for",j)
			pass
