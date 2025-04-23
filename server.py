import socket
import threading
from ssl_utils import wrap_socket

CONTROL_PORT = 9090
DATA_PORT = 9091
HOST = '0.0.0.0'

def handle_client(conn, addr):
    try:
        print(f"Connection attempt from {addr}")
        ssl_conn = wrap_socket(conn, is_server=True)
        data = ssl_conn.recv(1024)
        print(f"[SERVER] Received from {addr}: {data.decode()}")
        ssl_conn.send(b"Message received securely.")
        ssl_conn.close()
    except Exception as e:
        print(f"[SERVER] Error accepting connection: {e}")

def start_server(port):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, port))
    server_sock.listen(5)
    print(f"[{'CONTROL' if port == CONTROL_PORT else 'DATA'}] Listening on port {port}")
    while True:
        conn, addr = server_sock.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

threading.Thread(target=start_server, args=(CONTROL_PORT,), daemon=True).start()
threading.Thread(target=start_server, args=(DATA_PORT,), daemon=True).start()

# Keep main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("[SERVER] Shutting down.")
