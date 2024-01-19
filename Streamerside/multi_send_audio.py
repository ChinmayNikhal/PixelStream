import pyaudio
import socket
import threading

class AudioStreamServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.audio_started = False
        self.client_sockets = []  # List to store connected client sockets

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=2,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=4096)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # Allow up to 5 pending connections

        self.audio_started = True

        while self.audio_started:
            client_socket, address = self.server_socket.accept()
            self.client_sockets.append(client_socket)
            print(f"Client connected from {address}")

            # Create a thread for handling each client
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while self.audio_started:
                data = self.stream.read(4096)
                client_socket.sendall(data)
        except Exception as e:
            print(f"Error during audio streaming to client: {e}")
        finally:
            self.client_sockets.remove(client_socket)
            client_socket.close()
            print(f"Client disconnected")

    def stop(self):
        self.audio_started = False

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()
        for client_socket in self.client_sockets:
            client_socket.close()

if __name__ == '__main__':
    server = AudioStreamServer()
    server.start()

    # Optional: Add a way to stop the streaming (e.g., using keyboard input)
    # ...
