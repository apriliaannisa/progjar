import socketserver
import os

def bytes(number):
    hasil = bytearray()
    hasil.append(number & 255)
    for i in range(3):
        number = number >> 8
        hasil.append(number & 255)
    return hasil


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                data = self.request.recv(1024).decode()
                if os.path.exists(data):
                    length = os.path.getsize(data)
                    
                    with open(data, 'rb') as infile:
                        data = infile.read()

                    self.request.send(bytes(length)) # has to be 4 bytes
                    byte = 0
                    while byte < length:
                        self.request.send(data[byte:byte+1024])
                        byte += 1024
                    infile.close()
            except ConnectionAbortedError:
                print("No connection")
                break

if __name__ == "__main__":
    HOST = "localhost", 
    PORT = 6000

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()