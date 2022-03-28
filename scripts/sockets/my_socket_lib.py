import socket
import logging

from . import PARAM


class MySocket(socket.socket):
    pass


def connect_socket(host : str|int, url : str, port : int=80, print_host_ip : bool =True):
    # Instantiate and config socket
    my_socket = MySocket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to server over the internet
    my_socket.connect((host, port,), )
    access_cmd = "GET {} HTTP/1.0\r\n\r\n".format(url).encode()
    my_socket.send(access_cmd)

    # Print server name
    if print_host_ip and isinstance(host, str):
        # Return the name and ip of the host server
        host_ip_address = socket.gethostbyname(host)
        str1 = "The domain '{}' has an IP address of '{}'." \
        .format(host, host_ip_address)
        print(str1)

    while True:
        data = my_socket.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

    my_socket.close()