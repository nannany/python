if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    even_count = 0
    odd_count = 0
    for a in A:
        if a % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(3 ** N - (2 ** even_count))
