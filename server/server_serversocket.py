import socketserver 
import os

def konversibytes(no):
    hasil = bytearray()
    hasil.append(no & 255)
    for i in range(3): 
        no = no >> 8
        hasil.append(no & 255)
    return hasil

class TCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        while True:
            try:
                d = self.request.recv(1024).decode()
                if os.path.exists(d):
                    panjang = os.path.getsize(d)
                    
                    with open(d, 'rb') as file:
                        d = file.read() 
                        self.request.send(konversibytes(panjang)) 
                        byte = 0
                        while byte < panjang:
                            self.request.send(d[byte:byte+1024])
                            byte = byte + 1024

                file.close()
            except ConnectionAbortedError:
                print("No Connection")
                break

if __name__ == "__main__":
    # Buat server, sambung ke localhost pada port 9999
    with socketserver.TCPServer(('localhost', 5000), TCPHandler) as server:
        # Aktifkan server; ini akan terus berjalan sampai program di interupsi dengan Ctrl-C
        server.serve_forever()
