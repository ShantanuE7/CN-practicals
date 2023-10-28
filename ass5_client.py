import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
server_host = '127.0.0.1'
server_port = 8080

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive the welcome message from the server
welcome_message = client_socket.recv(1024)
print(welcome_message.decode())

while True:
    # Send data to the server
    message = input("Enter a message to send to the server (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.send(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

# Close the client socket
client_socket.close()
'''
Welcome to the server!
Enter a message to send to the server (or type 'exit' to quit): hello there!
Received: hello there!
Enter a message to send to the server (or type 'exit' to quit): exit


'''