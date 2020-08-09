Computer Networks
Assignment 1

Entry no. : 2017csb1061
Name: Abhinav Khanna

Part 1:

In part 1 of the assignment, we were supposed to run various debugging and troubleshooting commands, and display their outputs. All the command outputs are present in the file “Assignment_Outputs.odt”. 

Part 2:

In this section, we were supposed to use socket programming to create a client-server communication program, which was later extended to be a distributed server—client communication program. 
The steps to run the code are as follows:

1. Run the code “server_A.py”. It will ask for a port number.This is the port number which it will listen to for communication with the main server. Ensure that whatever port number is mentioned here is also mentioned in the file “routing_table.rtl” with the corresponding server name. 
2. Similarly, run codes “server_B.py”, “server_C.py”, and “server_D.py”.
3. Before we run the main server(the one that communicates directly with the client), open the file “routing_table.rtl”, and ensure that it has the correct IP addresses and port numbers corresponding to each server. This is because the main server consults this table to connect to servers A,B,C and D.
4. Run the code “server.py”. It will ask for another port number. This is the port number that the server will listen to, to connect and communicate with the client. 
5. Ensure that all five port numbers are distinct, and their value is greater than 1023(since port numbers less than, or equal to 1023 are reserved by the system).
6. Run the file “client.py”. It will ask for port number and Host IP address. Enter the port number of the main server, and it’s IP address. This will connect the client to the main server.
7. The client will then ask for username and password. Search results from all the servers will be displayed to the client. If “EXIT” is entered, then the connection will be terminated