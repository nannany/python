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

                one = str(target_digit) + "/" + str(target_digit)
                ele = "("
                for _ in range(round(math.sqrt(target_ans)) // target_digit):
                    ele += str(target_digit) + "+"
                for _ in range(round(math.sqrt(target_ans)) % target_digit):
                    ele += one + "+"
                ele = ele[:-1]
                ele += ")"
                ans += ele + "*" + ele
                if round(math.sqrt(target_ans)) ** 2 - target_ans > 0:
                    for _ in range((round(math.sqrt(target_ans)) ** 2 - target_ans) // target_digit):
                        ans += "-" + str(target_digit)
                    for _ in range((round(math.sqrt(target_ans)) ** 2 - target_ans) % target_digit):
                        ans += "-" + one
                else:
                    for _ in range((-round(math.sqrt(target_ans)) ** 2 + target_ans) // target_digit):
                        ans += "+" + str(target_digit)
                    for _ in range((-round(math.sqrt(target_ans)) ** 2 + target_ans) % target_digit):
                        ans += "+" + one

                if len(ans) > 31:
                    ans = ""
                    for _ in range(round(target_ans / target_digit)):
                        ans += str(target_digit) + "+"
                    ans = ans[:-1]
                    if round(target_ans / target_digit) * target_digit - target_ans > 0:
                        for _ in range(round(target_ans / target_digit) * target_digit - target_ans):
                            ans += "-" + one
                    else:
                        for _ in range(-round(target_ans / target_digit) * target_digit + target_ans):
                            ans += "+" + one

                print(ans)
                sock.send(ans.encode('utf-8'))


if __name__ == '__main__':
    main()
