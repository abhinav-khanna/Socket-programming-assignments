import csv
import socket

from thread import *
import threading

def check_attendance(username):
	flag = 0
	count = 0
	with open('attendance.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			# print(row[1])
			if username == row[1]:
				flag=1
				for i in row:
					if i == 'Done':
						count+=1

		if flag == 0:
			return -1

		else:
			# print(count)
			return (count)						
					
		

# print(check_attendance('2017csb1061@iitrpr.ac.in'))

def threaded_communication(conn,addr):
	print('Connection with {} client established'.format(addr))

	username = conn.recv(1024)
	print('Username {} received at server D'.format(username))
	
	# password = conn.recv(1024)
	# conn.send('Password received at server\nChecking checking checking credentials....')

	initial_result = check_attendance(username)
	print(initial_result)

	conn.sendall((str)(initial_result))

	conn.close()



s = socket.socket()

PORT = (int)(input("Enter port number to listen to main server(ensure that it is different from the main server)"))

s.bind(('',PORT))

s.listen(5)

while True:
	conn, addr = s.accept()

	start_new_thread(threaded_communication,(conn,addr,))


s.close()	
	

