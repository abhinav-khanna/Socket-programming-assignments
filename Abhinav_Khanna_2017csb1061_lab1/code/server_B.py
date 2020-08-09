import csv
import socket

from thread import *
import threading

def check_credentials(username,password):
	flag = 0
	with open('login_credentials_B.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			if username == row[0]:
				if password == row[1]:
					print('SERVER_B:Login Succesful')
					return 'SERVER_B:Login Succesful'
					flag = 1	

		if flag == 0:
			print('SERVER_B:Incorrect username/password')
			return 'SERVER_B:Incorrect username/password'


def threaded_communication(conn,addr):
	print('Connection with {} client established'.format(addr))

	username = conn.recv(1024)
	conn.send('Username {} received at server B'.format(username))
	
	password = conn.recv(1024)
	conn.send('Password {} received at server\nChecking checking checking credentials....'.format(password))

	initial_result = check_credentials(username,password)

	conn.sendall(initial_result)

	conn.close()



s = socket.socket()

PORT = (int)(input("Enter port number to listen to main server(ensure that it is different from the main server)"))

s.bind(('',PORT))

s.listen(5)

while True:
	conn, addr = s.accept()

	start_new_thread(threaded_communication,(conn,addr,))


s.close()	
	

