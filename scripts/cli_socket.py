import socket
import click
import time

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
access_cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysocket.send(access_cmd)

# timeout setup
st = time.monotonic()
dt = 0

while dt < 5:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")
    # update timeout
    dt = time.monotonic() - st
else:
    print("My timeout activated.")

mysocket.close()
