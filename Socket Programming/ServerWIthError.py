import socket                           # Import socket module
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
print("Socket created")

hostname = socket.gethostname()         # Get the local machine name
print("Local host:" + hostname)
port = 8888                             # Reserve a port for your service

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

# Keep talking to the client
while True:
    c, addr = s.accept()                # Establish connection with client
    print("Got connection from" + addr[0] + ":" + str(addr[1]))
    c.send("Connection complete")
    
c.close()                           # Close the connection 