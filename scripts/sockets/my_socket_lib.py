import socket
import urllib.request
import logging

from . import PARAM


class MySocket(socket.socket):
    pass


def connect_socket(host : 'str|int', url : str, port : int=80, print_host_ip : bool =True):
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

def create_server():
    print("Access http://localhost:{}".format(PARAM.DEF_WEBSERVER_PORT))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Configure socket to close properly? WORKS. https://stackoverflow.com/a/6380198/6556801
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        client_socket = None

        server_socket.bind((PARAM.DEF_SERVER_HOST, PARAM.DEF_WEBSERVER_PORT), )
        server_socket.listen(PARAM.DEF_SERVER_QUEUE_AMOUNT)
        while True:
            client_socket, address = server_socket.accept()     # Blocking, waiting for a request

            # Receive the information
            response_data = client_socket.recv(5000).decode()
            pieces_of_data = response_data.split("\n")
            if len(pieces_of_data) > 0:
                print(pieces_of_data[0])

            # Response details
            data = """HTTP/1.1 200 OK\r
            Content-Type: text/html; charset=utf-8\r
            \r
            <html><body>Hello world</body></html>\r
            \r
            """
            # alternative
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></htm    l>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(socket.SHUT_WR)
            
    except KeyboardInterrupt:
        print("""
        Shutting down...
        """)
    except Exception as e:
        print("Error:\n")
        print(e)
    finally:
        # client_socket.shutdown(socket.SHUT_WR)
        server_socket.close()

def url_request(url:str=PARAM.DEF_LOCAL_URL):
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        print(line.decode().strip())