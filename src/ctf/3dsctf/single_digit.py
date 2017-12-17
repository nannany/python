from __future__ import print_function
import socket
from contextlib import closing
import re
import math


def main():
    host = 'sdp01.3dsctf.org'
    port = 8003
    bufsize = 4096

    start = r"start:"
    re_start = re.compile(start)

    question = r'The number (\d+) using only the digit (\d+):'
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

                print(m.group(1))
                target_ans = int(m.group(1))
                print(m.group(2))
                target_digit = int(m.group(2))

                '''
              target_ans:だす答え
              target_digit:使う桁
              '''
                ans = ""

                if target_digit == 1:
                    for i in range(math.floor(math.log2(target_ans))):
                        ans += "(1+1)*"
                    ans = ans[:-1]
                    for i in range(target_ans - 2 ** math.floor(math.log2(target_ans))):
                        ans += "+1"
                    if len(ans) > 31:
                        ans = ""
                        for i in range(math.floor(math.log(target_ans,3))):
                            ans += "(1+1+1)*"
                        ans = ans[:-1]

                    print(ans)
                    sock.send(ans.encode('utf-8'))
                    continue

                if target_digit == 9:
                    if round(target_ans / 9) - target_ans / 9 > 0:
                        for i in range(round(target_ans / 9)):
                            ans += "9+"
                        ans = ans[:-1]
                        for i in range(round(target_ans / 9) * 9 - target_ans):
                            ans += "-9/9"

                        print(ans)
                        sock.send(ans.encode('utf-8'))
                        continue

                for i in range(target_ans // target_digit):
                    ans += str(target_digit) + '+'

                for i in range(target_ans % target_digit):
                    ans += str(target_digit) + "/" + str(target_digit) + "+"

                ans = ans[:-1]

                print(ans)
                sock.send(ans.encode('utf-8'))
        return


if __name__ == '__main__':
    main()
