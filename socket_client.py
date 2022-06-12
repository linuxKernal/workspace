import socket


HOST = '127.0.0.1'
PORT = 6001

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

msg = client.recv(1024)
print(msg.decode("utf-8"))

while True:
    msg = input("kali@root: ")
    if(msg=="exit1"):
        client.close()
        break
    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
