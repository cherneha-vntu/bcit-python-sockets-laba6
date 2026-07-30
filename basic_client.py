import socket

host = '127.0.0.1'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = "Hello world"
print(f"Sending to server: {message}")
client_socket.sendall(message.encode('utf-8'))

data = client_socket.recv(1024)
print(f"Received from server: {data.decode('utf-8')}")

client_socket.close()
