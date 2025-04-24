import socket
import base64
from ssl_utils import wrap_socket

def create_ssl_socket(host, port):
    raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw.connect((host, port))
    return wrap_socket(raw, server_hostname=host)

def simulate_encryption(msg):
    return base64.b64encode(msg.encode()).decode()

def simulate_decryption(enc_msg):
    return base64.b64decode(enc_msg.encode()).decode()

# IP and message
HOST = input("Enter server IP address: ")
CONTROL_PORT = 9090
DATA_PORT = 9091
user_msg = input("Enter the message to send: ")

# Encrypt message
encrypted_msg = simulate_encryption(user_msg)

# Display
print(f"[CLIENT] Sending original: {user_msg}")
print(f"[CLIENT] Sending encrypted: {encrypted_msg}")

# Encrypted message to control channel
control_sock = create_ssl_socket(HOST, CONTROL_PORT)
control_sock.sendall(encrypted_msg.encode())
control_response = control_sock.recv(1024).decode()
print(f"[CLIENT] Control response: {control_response}")
control_sock.close()

# Encrypted message to data channel
data_sock = create_ssl_socket(HOST, DATA_PORT)
data_sock.sendall(encrypted_msg.encode())
data_response = data_sock.recv(1024).decode()
print(f"[CLIENT] Data response: {data_response}")
data_sock.close()# # client.py
# import socket
# from ssl_utils import wrap_socket

# CONTROL_PORT = 9090
# DATA_PORT = 9091

# def create_ssl_socket(host, port):
#     raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     raw.connect((host, port))
#     return wrap_socket(raw, server_hostname=host)

# if _name_ == "_main_":
#     HOST = input("Enter the server IP address: ").strip()

#     control_sock = create_ssl_socket(HOST, CONTROL_PORT)
#     control_msg = "Hello from client (control)"
#     control_sock.sendall(control_msg.encode())
#     control_response = control_sock.recv(1024).decode()
#     print(f"[CLIENT] Sent: {control_msg}")
#     print(f"[CLIENT] Control response: {control_response}")
#     control_sock.close()

#     data_sock = create_ssl_socket(HOST, DATA_PORT)
#     data_msg = "Hello from client (data)"
#     data_sock.sendall(data_msg.encode())
#     data_response = data_sock.recv(1024).decode()
#     print(f"[CLIENT] Sent: {data_msg}")
#     print(f"[CLIENT] Data response: {data_response}")
#     data_sock.close()

# # client.py
# import socket
# from ssl_utils import wrap_socket

# CONTROL_PORT = 9090
# DATA_PORT = 9091

# def create_ssl_socket(host, port):
#     raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     raw.connect((host, port))
#     return wrap_socket(raw, server_hostname=host)

# if _name_ == "_main_":
#     HOST = input("Enter the server IP address: ").strip()

#     # Get user input messages
#     control_msg = input("Enter message for Control Channel: ").strip()
#     data_msg = input("Enter message for Data Channel: ").strip()

#     # Control Channel
#     control_sock = create_ssl_socket(HOST, CONTROL_PORT)
#     print(f"[CLIENT] Sending to Control Channel: {control_msg}")
#     print(f"[CLIENT] (Encrypted via SSL) {control_msg.encode('utf-8')}")
#     control_sock.sendall(control_msg.encode())
#     control_response = control_sock.recv(1024).decode()
#     print(f"[CLIENT] Control response: {control_response}")
#     control_sock.close()

#     # Data Channel
#     data_sock = create_ssl_socket(HOST, DATA_PORT)
#     print(f"[CLIENT] Sending to Data Channel: {data_msg}")
#     print(f"[CLIENT] (Encrypted via SSL) {data_msg.encode('utf-8')}")
#     data_sock.sendall(data_msg.encode())
#     data_response = data_sock.recv(1024).decode()
#     print(f"[CLIENT] Data response: {data_response}")
#     data_sock.close()

import socket
import base64
from ssl_utils import wrap_socket

def create_ssl_socket(host, port):
    raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw.connect((host, port))
    return wrap_socket(raw, server_hostname=host)

def simulate_encryption(msg):
    return base64.b64encode(msg.encode()).decode()

def simulate_decryption(enc_msg):
    return base64.b64decode(enc_msg.encode()).decode()

# IP and message
HOST = input("Enter server IP address: ")
CONTROL_PORT = 9090
DATA_PORT = 9091
user_msg = input("Enter the message to send: ")

# Encrypt message
encrypted_msg = simulate_encryption(user_msg)

# Display
print(f"[CLIENT] Sending original: {user_msg}")
print(f"[CLIENT] Sending encrypted: {encrypted_msg}")

# Encrypted message to control channel
control_sock = create_ssl_socket(HOST, CONTROL_PORT)
control_sock.sendall(encrypted_msg.encode())
control_response = control_sock.recv(1024).decode()
print(f"[CLIENT] Control response: {control_response}")
control_sock.close()

# Encrypted message to data channel
data_sock = create_ssl_socket(HOST, DATA_PORT)
data_sock.sendall(encrypted_msg.encode())
data_response = data_sock.recv(1024).decode()
print(f"[CLIENT] Data response: {data_response}")
data_sock.close()
