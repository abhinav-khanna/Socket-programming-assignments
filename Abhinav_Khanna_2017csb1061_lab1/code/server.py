import csv
import socket

from thread import *
import threading


def check_A(username,password,socket_a):
	socket_a.send(username)
	username_ack = socket_a.recv(1024)
	print(str(username_ack))
	
	socket_a.send(password)
	password_ack = socket_a.recv(1024)
	print(str(password_ack))

	initial_result_a = socket_a.recv(1024)

	# socket_a.close()

	print(initial_result_a)

	return initial_result_a

def check_B(username,password,socket_b):
	socket_b.send(username)
	username_ack = socket_b.recv(1024)
	print(str(username_ack))
	
	socket_b.send(password)
	password_ack = socket_b.recv(1024)
	print(str(password_ack))

	initial_result_b = socket_b.recv(1024)

	# socket_a.close()

	print(initial_result_b)

	return initial_result_b	

def check_C(username,password,socket_c):
	socket_c.send(username)
	username_ack = socket_c.recv(1024)
	print(str(username_ack))
	
	socket_c.send(password)
	password_ack = socket_c.recv(1024)
	print(str(password_ack))

	initial_result_c = socket_c.recv(1024)

	# socket_a.close()

	print(initial_result_c)

	return initial_result_c		


def check_credentials(username,password,socket_a,socket_b,socket_c):
	# flag = 0
	# with open('login_credentials.csv') as csv_file:
	# 	csv_reader = csv.reader(csv_file)
	# 	for row in csv_reader:
	# 		if username == row[0]:
	# 			if password == row[1]:
	# 				print('Login Succesful')
	# 				return 'Login Succesful'
	# 				flag = 1	

	# 	if flag == 0:
	# 		print('Incorrect username/password')
	# 		return 'Incorrect username/password'


	#this server will now act as a client to check
	#database of A,B,C and D

	# socket_a.connect((HOST_A,PORT_A))

	return (check_A(username,password,socket_a) + '\n' + check_B(username,password,socket_b) + '\n' + check_C(username,password,socket_c))



def check_attendance(username,socket_d):
	socket_d.send(username)
	data = socket_d.recv(1024)
	return data



def connect_to_A():
	# socket_a = socket.socket()

	HOST_A = raw_input('Enter Server A host IP address:')
	PORT_A = (int)(input('Enter PORT Number of A:'))

	# socket_a.connect((HOST_A,PORT_A))

	# print('Connected to server A')
	print('HOST_A:' + (str)(HOST_A) + ' PORT_A:' + (str)(PORT_A))

	return HOST_A,PORT_A


def connect_to_B():
	# socket_a = socket.socket()

	# HOST_B = raw_input('Enter Server B host IP address:')
	# PORT_B = (int)(input('Enter PORT Number of B:'))

	# socket_a.connect((HOST_A,PORT_A))

	# print('Connected to server A')

	print('HOST_B:' + (str)(HOST_B) + ' PORT_B:' + (str)(PORT_B))

	return HOST_B,PORT_B

def connect_to_C():
	# socket_a = socket.socket()

	HOST_C = raw_input('Enter Server C host IP address:')
	PORT_C = (int)(input('Enter PORT Number of C:'))

	# socket_a.connect((HOST_A,PORT_A))

	# print('Connected to server A')
	print('HOST_C:' + (str)(HOST_C) + ' PORT_C:' + (str)(PORT_C))

	return HOST_C,PORT_C


def connect_to_D():
	# socket_a = socket.socket()

	HOST_D = raw_input('Enter Server D host IP address:')
	PORT_D = (int)(input('Enter PORT Number of D:'))

	# socket_a.connect((HOST_A,PORT_A))

	# print('Connected to server A')
	print('HOST_D:' + (str)(HOST_D) + ' PORT_D:' + (str)(PORT_D))

	return HOST_D,PORT_D		





def threaded_communication(conn,addr,HOST_A,PORT_A,HOST_B,PORT_B,HOST_C,PORT_C,HOST_D,PORT_D):

	print('HOST_A:' + (str)(HOST_A) + ' PORT_A:' + (str)(PORT_A))
	socket_a = socket.socket()
	socket_a.connect((HOST_A,PORT_A))
	print('Connected to server A')

	print('HOST_B:' + (str)(HOST_B) + ' PORT_B:' + (str)(PORT_B))
	socket_b = socket.socket()
	socket_b.connect((HOST_B,PORT_B))
	print('Connected to server B')

	print('HOST_C:' + (str)(HOST_C) + ' PORT_C:' + (str)(PORT_C))
	socket_c = socket.socket()
	socket_c.connect((HOST_C,PORT_C))
	print('Connected to server C')

	print('HOST_D:' + (str)(HOST_D) + ' PORT_D:' + (str)(PORT_D))
	socket_d = socket.socket()
	socket_d.connect((HOST_D,PORT_D))
	print('Connected to server D')

	print('Connection with {} client established'.format(addr))
	username = conn.recv(1024)
	print("USERNAME:" + str(username))

	if username != 'EXIT':
		conn.send('This is acknowledgment that username {} has been received'.format(username))
		password = conn.recv(1024)

		print('username:' + username)
		print('password:' + password)

	if username == 'EXIT' or password == 'EXIT':
		# print('if case--------------------')
		conn.send('Terminating connection........')

		result = check_credentials('EXIT','EXIT',socket_a,socket_b,socket_c)

		attendance = (int)((check_attendance('EXIT',socket_d)))

		conn.send('Connection Terminated. Good Bye')
		conn.close()
		
	
	else:
		#print('else case------------------')
		conn.send('Password received\nChecking credentials.......')
		result = check_credentials(username,password,socket_a,socket_b,socket_c)

		attendance = (int)((check_attendance(username,socket_d)))
		print('attendance:' + (str)(attendance))
		if attendance == -1:
			conn.send('User does not exist in attendance database')

		else:
			if (attendance) < 6.4:
				conn.send('attendance is {}. Cannot provide access\n'.format(attendance))
			else:
				conn.send(result + '\nattendance:' + str(attendance)  + '\n Login Succesful\n')		
		# conn.send('Testing')
		conn.close()




with open('routing_table.rtl') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = '|')
		for row in csv_reader:
			if row[0] == 'A':
				HOST_A = row[1]
				PORT_A = int(row[2])

			elif row[0] == 'B':
				HOST_B = row[1]
				PORT_B = int(row[2])	

			elif row[0] == 'C':
				HOST_C = row[1]
				PORT_C = int(row[2])

			elif row[0] == 'D':
				HOST_D = row[1]
				PORT_D = int(row[2])		

# HOST_A, PORT_A = connect_to_A()
# HOST_B, PORT_B = connect_to_B()
# HOST_C, PORT_C = connect_to_C()
# HOST_D, PORT_D = connect_to_D()

PORT = (int)(input('Enter port number to listen to client:'))

s = socket.socket()

s.bind(('', PORT))

s.listen(5)

while True:
	conn, addr = s.accept()

	start_new_thread(threaded_communication,(conn,addr,HOST_A,PORT_A,HOST_B,PORT_B,HOST_C,PORT_C,HOST_D,PORT_D))
	



socket_a.close()
check_credentials(username, password)

s.close()
