while True:
    n = int(input())
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False

    p = 0

    for i in range(2, n + 1):
        if is_prime[i]:
            p += 1
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    print(p)
