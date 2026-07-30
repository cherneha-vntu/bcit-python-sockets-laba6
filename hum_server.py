import socket
import random
import time

# Humidity TCP server
host = '0.0.0.0'
port = 9002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Humidity server listening on port {port}...")

try:
    while True:
        connection_socket, addr = server_socket.accept()
        # Generate random humidity for Variant 24: 50 + random() * 24
        humidity = 50 + random.random() * 24
        response = str(humidity)
        connection_socket.send( (response + '\n').encode('utf-8'))
        time.sleep(0.5)
        connection_socket.close()
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    server_socket.close()
