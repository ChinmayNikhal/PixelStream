import cv2
import socket
import pickle
import struct

class VideoStreamClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.payload_size = struct.calcsize("Q")

    def start(self):
        print("Client connected to server.")
        while True:
            self._receive_and_display_frame()

    def _receive_and_display_frame(self):
        data = b""
        while len(data) < self.payload_size:
            packet = self.client_socket.recv(4 * 1024)  # 4K buffer size
            if not packet:
                self.stop()  # Server disconnected
                return
            data += packet

        packed_msg_size = data[:self.payload_size]
        data = data[self.payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += self.client_socket.recv(4 * 1024)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        cv2.imshow('Client', frame)

        if cv2.waitKey(1) == 13:
            self.stop()

    def stop(self):
        self.client_socket.close()
        cv2.destroyAllWindows()

# Create and start the client
client = VideoStreamClient('192.168.00.00', 8888)  # Replace with actual server IP
client.start()