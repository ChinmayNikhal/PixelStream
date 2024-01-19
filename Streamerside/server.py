import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.clients = []

    def start(self):
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Client connected from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            self.clients.append(client_socket)

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                self.chatbox_broadcast(data, client_socket)
            except ConnectionError:
                print(f"Client disconnected")
                self.clients.remove(client_socket)
                break

    def chatbox_broadcast(self, message, sender_socket=None):
        print(message)  # Display message in CLI chatbox
        for client_socket in self.clients:
            if client_socket != sender_socket:  # Don't send back to sender
                try:
                    client_socket.sendall(message.encode())
                except ConnectionError:
                    self.clients.remove(client_socket)

if __name__ == "__main__":
    server = ChatServer("0.0.0.0", 8080)  # Replace with your desired host and port
    server.start()
