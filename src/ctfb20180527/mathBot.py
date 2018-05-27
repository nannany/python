from __future__ import print_function
import socket
from contextlib import closing
import re


def main():
    host = '133.242.234.140'
    port = 8690
    bufsize = 4096

    pattern = r"\d+\s+[\\+-\\*/%]\s+\d+\s="
    repattern = re.compile(pattern)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.connect((host, port))
        while 1:
            byte_content = sock.recv(bufsize)
            unicode_string = byte_content.decode('utf-8')
            print(unicode_string)
            target_calc = unicode_string.split("\n")[-1]
            match_str = repattern.search(target_calc)
            operand1 = match_str.group().split()[0]
            operator = match_str.group().split()[1]
            operand2 = match_str.group().split()[2]
            ans = 0
            print(operand1 + operator + operand2)
            if operator == "+":
                ans = int(operand1) + int(operand2)
            if operator == "-":
                ans = int(operand1) - int(operand2)
            if operator == "*":
                ans = int(operand1) * int(operand2)
            if operator == "/":
                ans = int(operand1) // int(operand2)
            if operator == "%":
                ans = int(operand1) % int(operand2)
            ans_str = str(ans) + "\n"
            print(ans)
            sock.send(ans_str.encode('utf-8'))
        return


if __name__ == '__main__':
    main()
