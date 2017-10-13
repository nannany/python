import re

if __name__ == '__main__':
    N = int(input())
    s = input().strip('0')
    mojiretu_list = re.split('0{2,}', s)

    ans = 0

    for mojiretu in range(mojiretu_list):
        ichi_list = re.split('0', mojiretu)
        if len(ichi_list) == 1:
            continue
