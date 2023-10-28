import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = '127.0.0.1'
server_port = 8080

server_socket.bind((server_host, server_port))

server_socket.listen(5)
print(f"Server is listening on {server_host}:{server_port}")

while True:
   
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    message = "Welcome to the server!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    if not data:
        break

        
    print(f"Received: {data.decode()}")
    message= data.decode()
    client_socket.send(message.encode())
 
    client_socket.close()


server_socket.close()
'''
Server is listening on 127.0.0.1:8080
Accepted connection from ('127.0.0.1', 54808)
Received: hello there!

'''