import socket

host = '127.0.0.1'
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is listening on port 9999...")

try:
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from: {addr}")
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode('utf-8')
        print(f"Received message: {msg}")
        conn.sendall(msg.upper().encode('utf-8'))
        conn.close()
finally:
    server_socket.close()
