# Import socket programming library
import socket

# import thread module
from _thread import *
import threading 

print_lock = threading.Lock()

# Dictionary to diagnose the problem
def botDialogues(dictKey):
    botDict = {
        '1': "Forget Wi-Fi password",
        '2': "Wi-Fi signal",
        '3': "Restart router",
        '4': "Repair connection",
    }
    return botDict.get(dictKey)

# thread function
def threaded(c):
    while True:
        # data received from client (First response received from client and to introduce the bot)
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit (it will prevent the other user to access the same variable
            # in the server)
            #print_lock.release()
            break

        # send back the diagnose options back to client
        data = 'Response received, this is bot Wi-Fi please select the options for diagnose\n \
            1) Check Wi-Fi switch \
            2) Check Wi-Fi router \
            3) Repair connection \
            4) Exit'
        c.send(data.encode('ascii'))

        # option received from client (this is the second response received from client)
        option = c.recv(1024)
        option = str(option.decode('ascii'))
        print(option)

        if option == '4':
            break
    
        response = botDialogues(option)
        c.send(response.encode('ascii'))

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