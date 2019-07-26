import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def pscan(port):
    try:
        con = s.connect((target, port))
        return True
    except:
        return False