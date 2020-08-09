import socket
from threading import Timer
import time

def wait_ack(s,seq_number,frame_string,check_sum,flag):
	print('Waiting for acknowledgement. Retransmitting......')
	s.sendall(str(seq_number) + frame_string + chr(check_sum))

	ack = s.recv(2)

	if ack[0] == str(seq_number):
		# timer.cancel()
		# i+=100
		print('acknowledgement received')
		flag = 1
	
	print('-----------------------------------------')	
	return flag




def func():

	PORT_1 = (int)(input('Enter port_1 number(to connect to main server):'))
	HOST_1 = raw_input('Enter Host_1 IP address of main server:')

	PORT_2 = (int)(input('Enter port_2 number(to connect to main server):'))
	HOST_2 = raw_input('Enter Host_2 IP address of main server:')

	# PORT_1 = 12345
	# HOST_1 = '127.0.0.1'

	# PORT_2 = 23456
	# HOST_2 = '127.0.0.1'

	s1 = socket.socket()
	s2 = socket.socket()

	s1.connect((HOST_1, PORT_1))
	s2.connect((HOST_2, PORT_2))

	print('Connection with server established')


	username = raw_input('Enter username: ')
	# username = '2017csb1064@iitrpr.ac.in'

	if username == 'EXIT':
		s1.sendall(username)
		l1 = s1.recv(1024)
		print(l1)
		l2 = s1.recv(1024)
		print(l2)
		return s1,0

	s1.sendall(username)
	user_ack = s1.recv(1024)
	print(str(user_ack))

	password = raw_input('Enter password: ')

	# password = 'ADARSH'

	if password == 'EXIT':
		s1.sendall(password)
		l1 = s1.recv(1024)
		print(l1)
		l2 = s1.recv(1024)
		print(l2)
		return s1,0


	s1.sendall(password)
	password_ack = s1.recv(1024)
	print(str(password_ack))

	result = s1.recv(1024)
	print(str(result))

	if username == 'EXIT':
		s2.sendall(username)
		l1 = s2.recv(1024)
		print(l1)
		l2 = s2.recv(1024)
		print(l2)
		return s2,0

	s2.sendall(username)
	user_ack = s2.recv(1024)
	print(str(user_ack))

	if password == 'EXIT':
		s2.sendall(password)
		l1 = s2.recv(1024)
		print(l1)
		l2 = s2.recv(1024)
		print(l2)
		return s2,0


	s2.sendall(password)
	password_ack = s2.recv(1024)
	print(str(password_ack))

	result = s2.recv(1024)

	if ('SERVER_A:Login Succesful' not in result) and ('SERVER_B:Login Succesful' not in result) and ('SERVER_C:Login Succesful' not in result):
		print('Terminating connection with server')
		s1.sendall('100')
		s2.sendall('100')
		s1.sendall('The End-')
		s2.sendall('The End-')
		return s1,s2,0
	
	print(str(result))

	frame_size = int(input('Enter frame size:'))

	s1.sendall(str(frame_size))
	s2.sendall(str(frame_size))


	f = open('book.txt','r')

	total_string = f.read()

	i = 0

	seq_number = 0

	count = 0
	positive_count = 0
	negative_count = 0

	s = s1

	

	denom = int(input('Enter n, where probability of corrupted frame is 1/n:'))

	while i < len(total_string):

		count += 1
		if count%2 == 0:
			s = s1

		else:
			s = s2	

		frame_string = total_string[i:i+frame_size]

		check_sum = 0

		for j in range(i,min(i+frame_size,len(total_string))):
			check_sum = (check_sum + ord(total_string[j]))%94 + 33
		

		seq_number = (seq_number + 1)%2

		print('frame_string:' + frame_string)
		# print('size:' + str(len(frame_string)))
		print('check_sum:' + str(check_sum))
		# print(len(frame_string + chr(check_sum)))
		print('seq_number:' + str(seq_number))
		
		
		if count%denom == 1:
			s.sendall(str(seq_number) + frame_string + chr(check_sum + 1))
			negative_count += 1

		else:
			s.sendall(str(seq_number) + frame_string + chr(check_sum))
			positive_count += 1	


		ack = s.recv(2)
		
		if ack[0] == str(seq_number) and ack[1] == '1':
			print('positive acknowledgement received')
			i += frame_size
		
		else:
			print('negative acknowledgement received')
			print('Retransmitting.......')
			s.sendall(str(seq_number) + frame_string + chr(check_sum))
			ack = s.recv(2)

			print('positive acknowledgement for retransmission received')
			i += frame_size

	
	

		print('-----------------------------------------')	


	s1.sendall('The End-')
	s2.sendall('The End-')

	print('positive:' + str(positive_count))
	print('negative:' + str(negative_count))	

	return s1,s2,0


s1,s2,val = func()

if val == 0:
	s1.close()
	s2.close()	


