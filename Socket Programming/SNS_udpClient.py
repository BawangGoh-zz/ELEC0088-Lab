import socket
import sys

HOST = ''
PORT = 8888

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg:
    print ('Failed to create socket.')
    sys.exit()

host = 'localhost'
port = 8888

while True:
    msg = input('Enter message to send \n')
    msg = msg.encode()

    try:
        # Set the whole string
        s.sendto(msg, (host, port)) 

        # receive data from client (data, addr)
        d= s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply: ' + reply.decode())

    except socket.error as msg:
        print('Error code: ' +str(msg[0])+ 'Message ' +msg[1])
        sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print('Bind failed. Error code: ' +str(msg[0])+ 'Message ' +msg[1])
    sys.exit()
print('Socket bind complete')

# Now keep talking with the client
while True:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break
    reply = 'OK...' + data

    s.sendto(reply,addr)
    print('Message[' +addr[0]+ ':' +str(addr[1])+ '] - ' +data.strip())

s.close()

