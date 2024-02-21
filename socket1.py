import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", 3000))
soc.send(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")
reply = soc.recv(10000)
soc.shutdown(socket.SHUT_RDWR)
soc.close()
print(repr(reply))
