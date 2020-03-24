# Import socket programming library
import socket

# import thread module
from _thread import *
import threading 

print_lock = threading.Lock()

# thread function
def threaded(c):
    while True:
        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit (it will prevent the other user to access the same variable
            # in the server)
            #print_lock.release()
            break

        # Reverse the given string from client
        data = data[::-1]

        # send back reversed string to client 
        c.send(data)

    # connection closed
    c.close()

def main():
    host = ""

    # reverse a port on your computer 
    # in our case it is 12345 but it can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # Put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client (if the client try to overwrite the same variable in the server
        # in this case, we are not accessing any variable)
        #print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))

    s.close()

if __name__ == '__main__':
    main()