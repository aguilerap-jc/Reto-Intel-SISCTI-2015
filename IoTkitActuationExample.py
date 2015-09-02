import socket
import mraa
import json

UDP_IP = "127.0.0.1"
UDP_PORT = "41235"

myLed=mraa.Gpio(13)
myLed.dir(mraa.DIR_OUT)
componentName="led1"
sensorName="LED"

sock.bind((UDP_IP, UDP_PORT))

print "Listening on port", UDP_PORT

while True:
	data,addr=sock.recvform(4096)
	print "Recived", data, "form", addr[0]
	if addr[0] != "127.0.0.1":
		print "Rejecting external UDP message from", addr[0]
		continue
	js=json.loads(data)
	component=js["component"]
	command=js["command"]
	argvArray=js["argv"]
	if component == componentName:
		for argv in argvArray:
			name=argv['name']
			value=argv['value']
			print "name: "+name
			print "value: "+value
			if (name == sensorName):
				myLed.write(int(value))


