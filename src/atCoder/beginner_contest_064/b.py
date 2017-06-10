if __name__ == '__main__':
    N = int(input())

    a = list(map(int, input().split()))

    a.sort()

    print(a[-1] - a[0])
