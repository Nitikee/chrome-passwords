import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
BUFF_SIZE = 1024
s.bind(('',port))
s.listen(5)

while True:
	print ('waiting for a connection...')
	c, addr = s.accept()
	print('connected to',addr)
	myfile = open('file.json','w')
	while True:
		data = c.recv(1024).decode()
		myfile.write(data)
		if not data:
			myfile.close()
			break
	myfile.close
	c.close
	s.close
