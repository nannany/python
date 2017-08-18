import decimal


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def lcm(a, b):
    g = euclid(a, b)
    print(g)
    print(a * b)

    return int(a / g * b)


if __name__ == '__main__':
    N = int(input())
    ans = 1
    for i in range(N):
        T = int(input())
        ans = lcm(ans, T)

    print(ans)
