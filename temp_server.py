import socket
import random
import time

# Temperature TCP server
host = '0.0.0.0'
port = 9001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Temperature server listening on port {port}...")

try:
    while True:
        connection_socket, addr = server_socket.accept()
        # Generate random temperature for Variant 24: 20 + random() * 24
        temp = 20 + random.random() * 24
        response = str(temp)
        connection_socket.send( (response + '\n').encode('utf-8'))
        time.sleep(0.5)
        connection_socket.close()
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    server_socket.close()
