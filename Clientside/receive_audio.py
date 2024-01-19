import pyaudio
import socket
import time

class AudioStreamClient:
    def __init__(self, host='192.168.64.159', port=8080):
        self.host = host
        self.port = port
        self.audio_started = False  # Flag to track stream status

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=2,
                                  rate=44100,
                                  output=True,
                                  frames_per_buffer=4096)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        self.audio_started = True

        try:
            while self.audio_started:
                data = self.client_socket.recv(4096)
                self.stream.write(data)  # Play received audio data
                print("Receiving")  # Optional: Print a message
        except Exception as e:
            print(f"Error during audio streaming: {e}")
        finally:
            self.cleanup()

    def stop(self):
        self.audio_started = False  # Signal the loop to stop

    def cleanup(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.client_socket.close()

if __name__ == '__main__':
    client = AudioStreamClient()
    client.start()  # Start the audio streaming

    # Optional: Add a way to stop the streaming (e.g., using keyboard input)
    # ...
