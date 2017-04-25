def get_gcd(_a, _b):
    if _a % _b == 0:
        return _b
    return get_gcd(_b, _a % _b)


if __name__ == '__main__':
    while True:
        a, b = list(map(int, input().split()))
        gcd = get_gcd(a, b)
        lcm = a * b / gcd
        print(str(gcd) + " " + str(int(lcm)))
