import socket


def func():

	PORT = (int)(input('Enter port number(to connect to main server):'))
	if PORT == 'EXIT':
		return 0
	HOST = raw_input('Enter Host IP address of main server:')
	if HOST == 'EXIT':
		return 0

	s = socket.socket()

	s.connect((HOST, PORT))

	print('Connection with server established')

	username = raw_input('Enter username: ')

	if username == 'EXIT':
		s.sendall(username)
		l1 = s.recv(1024)
		print(l1)
		l2 = s.recv(1024)
		print(l2)
		return s,0

	s.sendall(username)
	user_ack = s.recv(1024)
	print(str(user_ack))

	password = raw_input('Enter password: ')

	if password == 'EXIT':
		s.sendall(password)
		l1 = s.recv(1024)
		print(l1)
		l2 = s.recv(1024)
		print(l2)
		return s,0


	s.sendall(password)
	password_ack = s.recv(1024)
	print(str(password_ack))

	result = s.recv(1024)
	print(str(result))

	return s,0


s,val = func()

if val == 0:
	s.close()	


