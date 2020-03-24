import socket               # Import socket module
import sys
import _thread

#Function for handling connections. This will be used to create threads
def clientthread(c):
    #Sending message to connected client
	#c.send('Welcome to the server. Type something and hit enter\n') #send only takes string
	
	#infinite loop so that function do not terminate and thread do not end.
	while True:	
		#Receiving from client
		data = c.recv(1024)
		reply = 'OK...' + data
		if not data: 
			break
	
		c.sendall(reply)
	
	#came out of loop
	c.close()

def main():
    hostname = socket.gethostname()         # All available interfaces
    print(hostname)         # Print local host name
    port = 8888             # Reserve a port for your service

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
    print("Socket created")

    # Bind socket to local host and port
    try:
        s.bind((hostname,port))                 # Bind to the port
    except socket.error as msg:
        print("Bind failed. Error code: " + str(msg[0]) + "Message" + msg[1])
        sys.exit()
    print("socket bind complete")

    # Waiting for client connection
    s.listen(5)                             # 5 mean connections and the 6th socket will be refused
    print("Socket listening")

    #now keep talking with the client
    while True:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print ("Connected with " + addr[0] + ':' + str(addr[1]))
        
        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        _thread.start_new_thread(clientthread, (conn, ))

    s.close()

if __name__ == "__main__":
	main();		
