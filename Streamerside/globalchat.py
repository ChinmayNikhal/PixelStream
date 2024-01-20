import socket

class GlobalChat:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = "GlobalChat"

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"GlobalChat connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Connection refused by server")

    def run(self):
        self.connect()
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if not data:
                    break
                print(data)  # Print received message to CLI
            except ConnectionError:
                print("Connection to server lost")
                break

# Example usage:
if __name__ == "__main__":
    global_chat = GlobalChat("192.168.0.0", 8080)  # Replace with server's host and port
    global_chat.run()
