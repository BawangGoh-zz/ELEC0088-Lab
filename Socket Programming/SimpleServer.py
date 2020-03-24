import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8888                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    print("Waiting for connection")
    c, addr = s.accept()     # Establish connection with client.
    print("Connection established with", addr)
    c.send("Thank you for connecting")

c.close()                   # Close the connection