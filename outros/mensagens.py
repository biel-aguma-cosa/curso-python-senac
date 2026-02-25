import socket
import threading

running = True
host, port = 'localhost', '21110'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen(8)

def loop(client,address):
    pass

while running:
    client, address = server.accept()
    
    thread = threading.Thread(target=loop,args=(client,address))
    thread.start()