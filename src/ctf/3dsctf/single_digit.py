from __future__ import print_function
import socket
from contextlib import closing
import re
import math
import sympy


def get_ans(_target_ans):
    ans = ""
    ele = "("
    global one
    global target_digit
    for _ in range(round(math.sqrt(_target_ans)) // target_digit):
        ele += str(target_digit) + "+"
    for _ in range(round(math.sqrt(_target_ans)) % target_digit):
        ele += one + "+"
    ele = ele[:-1]
    ele += ")"
    ans += ele + "*" + ele
    if round(math.sqrt(_target_ans)) ** 2 - _target_ans > 0:
        for _ in range((round(math.sqrt(_target_ans)) ** 2 - _target_ans) // target_digit):
            ans += "-" + str(target_digit)
        for _ in range((round(math.sqrt(_target_ans)) ** 2 - _target_ans) % target_digit):
            ans += "-" + one
    else:
        for _ in range((-round(math.sqrt(_target_ans)) ** 2 + _target_ans) // target_digit):
            ans += "+" + str(target_digit)
        for _ in range((-round(math.sqrt(_target_ans)) ** 2 + _target_ans) % target_digit):
            ans += "+" + one

    return ans


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
                global target_digit
                target_digit = int(m.group(2))

                '''
              target_ans:だす答え
              target_digit:使う桁
              '''
                # oneの定義をする
                global one
                if target_digit == 1:
                    one = "1"
                else:
                    one = str(target_digit) + "/" + str(target_digit)

                ans = get_ans(target_ans)

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

                if len(ans) > 31:
                    ans = ""
                    factors = sympy.factorint(target_ans)
                    for fact, num in factors.items():
                        if fact < 11:
                            ele = "("
                            for _ in range(fact // target_digit):
                                ele += str(target_digit) + "+"
                            for _ in range(fact % target_digit):
                                ele += one + "+"

                            ele = ele[:-1] + ")"
                        else:
                            ele = "(" + get_ans(fact) + ")"
                        for _ in range(num):
                            ans += ele + "*"

                    ans = ans[:-1]

                print(ans)
                sock.send(ans.encode('utf-8'))


if __name__ == '__main__':
    main()
