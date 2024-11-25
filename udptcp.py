#tcp clientSocket
from socket import *
serverport=8008
serverhost='127.0.0.1'

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverhost,serverport))

messageSent=input("enter the Math che phy mark: ")

clientSocket.send(messageSent.encode())
messageRec=clientSocket.recv(1024).decode()
print(messageRec+" got from servere")

clientSocket.close()

#tcp Server
from socket import *
port=8008
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(1)
print("listening to {port}")

while True:
 connectionSocket,add=serverSocket.accept()
 message=connectionSocket.recv(1024).decode()

 math,che,phy=message.split()
 math=float(math)
 phy=float(phy)
 che=float(che)
 result=math+(phy+che)/2
 connectionSocket.send(str(result).encode())

connectionSocket.close()

#udp clientSocket
from socket import *

hostname='127.0.0.1'
port=8009

clientSocket=socket(AF_INET,SOCK_DGRAM)

message=input('enter the tempconverion temperature')

clientSocket.sendto(message.encode(),(hostname,port))

messageRec,serveradd=clientSocket.recvfrom(1024)
print(messageRec.decode())
clientSocket.close()

#udpserver 
from socket import *

port=8009
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',port))

while True:
    message,clientAdd=serverSocket.recvfrom(1024)

    message=message.decode()

    conv,temp=message.split()

    if conv=="CtoF":
     message=(float(temp)*(9/5))+32
    elif conv=="FtoC":
     message=(float(temp)-32)*(5/9)
    else:
     message="invalid format"
    serverSocket.sendto(str(message).encode(),clientAdd)

