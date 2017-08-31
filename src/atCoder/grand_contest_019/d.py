if __name__ == '__main__':
    A = list(input())
    B = list(input())
    if B.count("1") == 0:
        if A.count("1") == 0:
            print(0)
        else:
            print(-1)

