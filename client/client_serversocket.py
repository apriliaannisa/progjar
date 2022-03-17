import socket
import sys


HOST = "localhost"
PORT = 5000

server_address = (HOST, PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

try:
    while True:
        
        c = input("->")
        x = c.split()

        if x[0] == "unduh":
            client_socket.send(x[1].encode())

            sign = 0
            with open(x[1], "wb") as file:
                d = client_socket.recv(1024)
                while d:
                    if sign != 0: 
                        file.write(d)
                    if (len(d) < 1024):
                        break
                    else: d = client_socket.recv(1024)
                    sign += 1

            file.close()

except KeyboardInterrupt:  
    client_socket.close()
    sys.exit(0)

