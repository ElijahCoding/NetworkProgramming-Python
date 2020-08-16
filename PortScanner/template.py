import socket
import threading
from queue import Queue

target = '127.0.0.1'
# queue = Queue()
# open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(1, 10000):
    result = portscan(port)
    if result:
        print("Port {} is open !".format(port))