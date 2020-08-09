import csv
import socket

from thread import *
import threading

def check_credentials(username,password):
	flag = 0
	with open('login_credentials_C.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if username == row[0]:
				if password == row[1]:
					print('SERVER_C:Login Succesful')
					return 'SERVER_C:Login Succesful'
					flag = 1	

		if flag == 0:
			print('SERVER_C:Incorrect username/password')
			return 'SERVER_C:Incorrect username/password'


def threaded_communication(conn,addr):
	print('Connection with {} client established'.format(addr))

	username = conn.recv(1024)
	conn.send('Username {} received at server C'.format(username))
	
	password = conn.recv(1024)
	conn.send('Password {} received at server\nChecking checking checking credentials....'.format(password))

	initial_result = check_credentials(username,password)

	conn.sendall(initial_result)

	frame_size = int(conn.recv(5))
	print('frame_size:' + str(frame_size))

	received_string = ''
	net_string = ''

	while True:
		received_string = conn.recv(frame_size + 2)
		print(received_string[1:-1])
		net_string += received_string[1:-1]
		print('-------------------------------------------')
		# conn.sendall('11')

		if received_string[-8:-1] == 'The End' or len(received_string) == 0:
			print('Breaking out of while loop')
			break

	print(net_string)
	conn.close()



s = socket.socket()

PORT = (int)(input("Enter port number to listen to main server(ensure that it is different from the main server)"))

s.bind(('',PORT))

s.listen(5)

while True:
	conn, addr = s.accept()

	start_new_thread(threaded_communication,(conn,addr,))


s.close()	
	

