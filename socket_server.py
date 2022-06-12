import socket
import subprocess
HOST = '127.0.0.1'
PORT = 6001

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)


print("Server listening...")
clientsocket, address = server.accept()
print(f"Connection from {address[0]} has been established.")
clientsocket.send("Server successfully connected".encode('utf-8'))
while True:
    msg = clientsocket.recv(1024).decode('utf-8')
    if(msg=="terminate"):
        clientsocket.send("connection terminate".encode('utf-8'))
        clientsocket.close()
        break
    else:
        if(msg=="list socket"):
            msg="netstat -tulpn"
        elif(msg=="start"):
            msg="gnome-terminal -- bash -c 'nc -ln -p 1234'"
        elif(msg.split()[0]=="alert"):
            msg = "notify-send "+msg.split()[1]
        run = subprocess.Popen(msg, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result,error = run.communicate()
        if error:
            clientsocket.send(error)
        elif result:
            clientsocket.send(result)
        else:
            clientsocket.send("Done".encode('utf-8'))
clientsocket.close()
