# Build a basic chat server where multiple clients can connect and communicate simultaneously. 
# Each client connection should be handled by a separate thread, showing how multithreading is essential 
# for handling multiple users in real time.py

# SERVER CODE
"""
import socket
import threading

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Chat server started on {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("New connection from {}".format(client_address))
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

start_server('127.0.0.1', 5555)
"""



#CLIENT CODE
"""
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            break

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            print("Connection closed.")
            break

start_client('127.0.0.1', 5555)
"""
