# client.py
import socket
from ssl_utils import wrap_socket

HOST = '127.0.0.1'         # Server IP address
CONTROL_PORT = 9090        # Control channel port
DATA_PORT = 9091           # Data channel port

def create_ssl_socket(host, port):
    raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw.connect((host, port))
    return wrap_socket(raw, server_hostname=host)

# Connect to the control channel
control_sock = create_ssl_socket(HOST, CONTROL_PORT)
control_msg = "Hello from client (control)"
control_sock.sendall(control_msg.encode())
control_response = control_sock.recv(1024).decode()
print(f"[CLIENT] Sent: {control_msg}")
print(f"[CLIENT] Control response: {control_response}")
control_sock.close()

# Connect to the data channel
data_sock = create_ssl_socket(HOST, DATA_PORT)
data_msg = "Hello from client (data)"
data_sock.sendall(data_msg.encode())
data_response = data_sock.recv(1024).decode()
print(f"[CLIENT] Sent: {data_msg}")
print(f"[CLIENT] Data response: {data_response}")
data_sock.close()
