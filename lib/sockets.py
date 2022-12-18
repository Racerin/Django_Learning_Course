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
