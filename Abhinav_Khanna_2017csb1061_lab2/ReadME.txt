In this assignment, I have extended the functionality
implemented in the first assignment. The new features added are:

1: A text file is now transferred from the client to the server. Text is read,
and divided into substrings, which is encapsulated as frames, and sent over the 
network, where the frames are decapsulated and recombined to form the original file.
The client can decide the size of the frames to be sent.

2: Instead of a single intermediate server,as used in the previous assignment,
there are two identical intermediate servers available to the client, to increase 
reliability of the overall system. The client is aware of both of these servers, and
frames are sent from to each of these servers alternatively by the client node.

3: Error checking has also been introduced. The frame, apart from the data, also
contains a checksum value. The checksum value is calculated at both client and server nodes,
and if the value does not match, the frame is dropped, and the client re-sends the frame.

	To simulate error checking, errors are introduced intentionally into frames with some
probability, which is also asked from the user.

HOW TO RUN THE PROGRAM:

1: Go to the folder named 'code'.
2: Run the program server_A.py. It will ask for a port number. Enter any value greate than 1023.
3: Follow similar steps to run programs server_B.py, server_C.py, and server_D.py. For each of the 
	servers, ensure that the port numbers are distinct.
4: Open the file routing_table.rtl. Ensure that the host numbers and port numbers for servers A,B,C,D
	are the same as those asked for by the program. This routing table will be used by the intermediate
	server(s) 
5: Run the program server.py in two seperate terminals, each time with different port numbers.
6: Run the program client.py. It will ask for the host and port numbers for both of the intermediate
	servers. 
7: Enter username and password. If login is unsuccesful, the client program will terminate.
8: If login is succesful, it will ask for frame size and probability for error.
9: Then, it will start reading the text from the file 'book.txt', and start sending it to the server.		