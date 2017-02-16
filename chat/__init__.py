import socket, sys;
from threading import *

port = 7777
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket = None

def setupTheProgramForKelly():
    global sock,clientsocket
    sock.bind(("127.0.0.1",port))
    sock.listen(3)
    print("Waiting for connection on port",str(port) + "...")
    clientsocket = sock.accept()
    print("Connection received!\n")
    Thread(target=receive_serv).start()  
    serverLoop()
    return;

def setupTheProgramForCyle():
    global sock
    print("Trying to connect now...")
    #sock.settimeout(1)
    connectionMade = False
    for x in range(20):
        try:
            print("Connection attempt",(x+1),"out of 20")
            sock.connect(("127.0.0.1",7777))
            connectionMade=True
            break
        except ConnectionRefusedError as e:
            print("Connection refused.")
    if connectionMade:
        print("Connection established!\n")
        Thread(target=receive).start()
        clientLoop()  
        #Thread(target=recv_msg, args=(sockfd,)).start()
    else:
        print("\nFailed to establish connection to server.  Relaunching...\n")
        getTypeFromUser()
    return;

def getTypeFromUser():
    whatTheUserTypesIn = input("Please choose how the program should operate:\n1. Server mode (for Kelly)\n2. Client mode (for Cyle)\n3. Exit\n")
    
    if whatTheUserTypesIn == "1":
        setupTheProgramForKelly()
        
    elif whatTheUserTypesIn == "2":
        setupTheProgramForCyle()
        
    elif whatTheUserTypesIn == "3":
        sys.exit()
        
    else:
        print("You done fucked up son.  I'm gonna give you another try\n\n")
        getTypeFromUser()
    return;

def clientLoopOld():
    global sock
    while True: 
        try:
            data = sock.recv(1024)
            data = data.decode()
            print(data)
        except Exception as e:
            print("Timed out...")
        
        package=input("Please type a message to send: ")
        sizeOfPackage = sys.getsizeof(package)
        print("Package size is",sizeOfPackage,"bytes.")
        message_bytes = package.encode()
        print(message_bytes)
        sock.send(message_bytes)
    return;

def serverLoop():
    global clientsocket
    while True:
        xyz = input("Type the message to send: ")
        zyx = xyz.encode('utf-8')
        clientsocket[0].sendall(zyx)
    return;

def clientLoop():
    global sock
    while True:
        xyz = input("Type the message to send: ")
        zyx = xyz.encode('utf-8')
        sock.sendall(zyx)
    return;

def printIntro():
    print("+---------------------------------------+")
    print("|    Welcome to Cyle's Chat Program!    |")
    print("+---------------------------------------+\n\n")
    return;


#Threaded functions for receiving and sending

def send_msg(livesock):
    while True:
        data = input()
        data = data.encode(encoding='utf_8', errors='strict')
        livesock.send(data)
    return;

def receive():
    global sock
    while True:
        data = sock.recv(1024)
        if not data: sys.exit(0)
        abc = data.decode('utf-8')
        print("Message received:",abc)
    return;

def receive_serv():
    global clientsocket
    while True:
        data = clientsocket[0].recv(1024)
        if not data: sys.exit(0)
        abc = data.decode('utf-8')
        print("Message received:",abc)
    return;
# The actual program starts here!


printIntro()
getTypeFromUser()

