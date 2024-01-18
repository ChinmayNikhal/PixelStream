import socket
import cv2
import pickle
import struct
import select

class VideoStreamServer:
    def __init__(self, host='0.0.0.0', port=8888):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.clients = []
        self.cap = None  # Initialize video capture later

    def start(self):
        print("Server is listening...")
        while True:
            ready_to_read, _, _ = select.select([self.server_socket], [], [], 0.1)
            if ready_to_read:
                client_socket, client_address = self.server_socket.accept()
                print(f"Client connected: {client_address}")
                self.clients.append(client_socket)

            try:
                self._handle_frame_capture_and_streaming()
            except Exception as e:
                print(f"Error: {e}")
                break  # Exit if an unexpected error occurs

    def _handle_frame_capture_and_streaming(self):
        if not self.cap:  # Initialize video capture once
            self.cap = cv2.VideoCapture(0)

        ret, frame = self.cap.read()

        if ret:
            frame_data = pickle.dumps(frame)
            message_size = struct.pack("Q", len(frame_data))

            for client_socket in self.clients:
                try:
                    client_socket.sendall(message_size)
                    client_socket.sendall(frame_data)
                except ConnectionError:
                    self.clients.remove(client_socket)
                    print(f"Client disconnected: client_address")

            cv2.imshow('Server', frame)
            if cv2.waitKey(1) == 13:  # Exit on 'Enter' key
                self.stop()

    def stop(self):
        self.cap.release()
        for client_socket in self.clients:
            client_socket.close()
        self.server_socket.close()

# Create and start the server
server = VideoStreamServer()
server.start()
