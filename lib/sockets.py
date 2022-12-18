import socket

def read_webpage(domain:str, url:str, port=80, stream_size=512) -> str:
    # Instantiate socket connection over the internet
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((domain, port))
    # Format the request for website
    cmd = 'GET {} HTTP/1.0\r\n\r\n'.format(url).encode()

    # Extract the text from the response
    mysock.send(cmd)
    data = ""
    while True:
        sub_data = mysock.recv(stream_size)
        if len(sub_data) < 1:
            break
        data += sub_data.decode() + " "
    
    # Clean-up and return data
    mysock.close()
    return data

def read_webpage_example(verbose=True) -> str:
    ans = read_webpage('data.pr4e.org', "http://data.pr4e.org/page1.htm")
    if verbose:
        print(ans)
    return ans

def web_server(ip_address:str='localhost', port:int=9000, def_msg:str="Hello World", log_func=print) -> None:
    """ 
    Create a server and let clients connect to it to request a webpage message.
    ip_address: hostname or IPv4 address of server (this device)
    port: port number on which server communicates out of
    def_msg: Text message website user sees.
    log_func: Function used to log information within this function to admin. All logs are on one level
    """
    log_func("Access http://{}:{}".format(ip_address, port) )
    try:
        # Create socket (phone call) and ensure the port is available
        server_socekt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socekt.bind((ip_address, port))
        server_socekt.listen(5)
        while(True):
            # Initiate web user communication and receives user HTTP request
            (clientsocket, address) = server_socekt.accept()
            rec_data = clientsocket.recv(5000).decode()
            pieces = rec_data.split("\n")
            if (len(pieces) > 0):
                log_func(pieces[0])
            
            # Respond to web user
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>{}</body></html>\r\n\r\n".format(def_msg)
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        log_func("\nShutting down...\n")
    except Exception as exc:
        log_func("Error:\n")
        log_func(exc)
    finally:
        server_socekt.close()
        log_func("Socket 'http://{}:{}' closed.".format(ip_address, port))
