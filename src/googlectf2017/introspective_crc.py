import socket
from contextlib import closing

if __name__ == '__main__':
    host = 'selfhash.ctfcompetition.com'
    port = 1337
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with closing(sock):
        sock.connect((host, port))
        while True:
            byte_content = sock.recv(bufsize)
            unicode_string = byte_content.decode('utf-8')
            print(unicode_string)
            res_str = "0000000000000000001111010111001010010011111001001101011101010001001011100001011100" + "\n"
            sock.send(res_str.encode('utf-8'))
