import sys

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    min_num = min(a)
    max_num = max(a)

    if max_num - min_num >= 2:
        print("No")
    elif max_num == min_num :
        if max_num == N -1 or 2*max_num <= N:
            print("Yes")
        else:
            print("No")
    else:
        x = a.count(min_num)
        y = a.count(max_num)
        if x < max_num and 2 * (max_num - x) <= y:
            print("Yes")
        else:
            print("No")