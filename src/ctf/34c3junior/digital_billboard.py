from __future__ import print_function
import socket
from contextlib import closing

if __name__ == '__main__':
    host = '35.198.185.193'
    port = 1337
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        while True:
            byte_content = sock.recv(bufsize)
            unicode_string = byte_content.decode('utf-8')
            print(unicode_string)
            sock.send('modinfo\n'.encode('utf-8'))
