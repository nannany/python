if __name__ == '__main__':
    N = int(input())
    K = int(input())

    num = 1
    for i in range(N):
        if num <= K:
            num *= 2
        else:
            num += K

    print(num)
