from __future__ import print_function
import socket
from contextlib import closing
import re
from collections import deque
import string

if __name__ == '__main__':
    host = 'capoditutticapi01.3dsctf.org'
    port = 8001
    bufsize = 4096

    start = r"note:"
    re_start = re.compile(start)

    question = ': \[([A-Z]+), (\d+), (.+)\]'
    re_question = re.compile(question)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        while True:
            byte_content = sock.recv(bufsize)
            unicode_string = byte_content.decode('utf-8')
            print(unicode_string)
            if re_start.search(unicode_string):
                sock.send('start\n'.encode('utf-8'))
                continue
            m = re_question.search(unicode_string)
            if m:
                alp = deque(string.ascii_uppercase)
                alp.rotate(int(m.group(2)))
                key = m.group(1)
                print(alp)
                ans = ""

                for moji in m.group(3):
                    if moji == " ":
                        ans += " "
                    elif moji == ",":
                        ans += ","
                    elif moji == ".":
                        ans += "."
                    elif moji == "à":
                        ans += "à"
                    else:
                        ans += alp[key.find(moji)]

                print(ans)
                sock.send(ans.encode('utf-8'))
