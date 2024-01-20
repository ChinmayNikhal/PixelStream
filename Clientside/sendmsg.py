import socket

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Connection refused by server")
            
    def get_username(self):
        while not self.username:
            username = input("Enter your username (or leave blank to use your IP): ")
            if not username:
                self.username = self.client_socket.getsockname()[0]  # Use IP as username
            else:
                self.username = username

    def send_message(self, message):
        try:
            formatted_message = f"{self.username}: {message}"
            self.client_socket.sendall(formatted_message.encode())
            # self.client_socket.sendall(message.encode())
        except ConnectionError:
            print("Connection to server lost")

if __name__ == "__main__":
    client = ChatClient("192.168.0.0", 8080)  # Replace with server's host and port
    client.connect()
    client.get_username()
    
    while True:
        msg = input()
        client.send_message(msg)
