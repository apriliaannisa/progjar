import socket
import sys

HOST = "localhost"
PORT = 6000
server_address = (HOST, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    while True:
        
        c = input("--->")
        x = c.split()

        if x[0] == "unduh":
            client_socket.send(x[1].encode())

            flag = 0
            with open(x[1], "wb") as file:
                data = client_socket.recv(1024)
                while data:
                    if flag != 0:
                        file.write(data)
                    if (len(data) < 1024):
                        break
                    else:
                        data = client_socket.recv(1024)
                    flag = flag + 1

            file.close()

except KeyboardInterrupt:
    client_socket.close()
    sys.exit(0)