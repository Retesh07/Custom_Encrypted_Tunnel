# Custom Encrypted Tunnel

This project implements a custom encrypted tunnel using raw sockets in Python. It is designed to provide secure, low-level communication between a client and server using SSL/TLS encryption over two separate channels — one for control and another for data. The system is scalable, supports multiple clients and servers without the need for rewriting or recompiling the code, and ensures encrypted data transmission over the network.

## 🔐 Overview

The tunnel leverages both **raw sockets** for low-level packet control and **SSL encryption** for secure communication. It splits the communication process into two dedicated channels:

- **Control Channel** (Port `9090`): Manages session control and command signaling between the client and server.
- **Data Channel** (Port `9091`): Handles the transmission of encrypted payload data.

Both channels operate in parallel and are encrypted using custom SSL certificates. The system is robust, modular, and supports graceful termination to prevent issues such as port binding errors.

## 💡 Key Features

- **SSL/TLS Encryption**: Ensures confidentiality and data integrity using custom certificates.
- **Dual-Channel Architecture**: Separates control and data planes for organized communication.
- **Raw Socket Implementation**: Offers deep network-level control, suitable for learning and custom protocol development.
- **Multi-client/Server Support**: Dynamic, scalable system without code modifications.
- **Graceful Shutdown**: Clean disconnection handling with no residual binding or orphaned sockets.

SSL-encrypted connections with the server — one for control and one for data.
