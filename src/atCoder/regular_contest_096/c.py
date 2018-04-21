if __name__ == '__main__':
    A, B, C, X, Y = map(int, input().split())

    if (A - 2 * C) >= 0 and (B - 2 * C) >= 0:
        print(max(2 * C * X, 2 * C * Y))
    elif (A - 2 * C) <= 0 and (B - 2 * C) <= 0:
        print()
    elif (A - 2 * C) < 0 and (B - 2 * C) > 0:
        if Y < X:
            print(A * (Y - X) + 2 * C * Y)
        else:
            print(max(2 * C * X, 2 * C * Y))
    elif (A - 2 * C) > 0 and (B - 2 * C) < 0:
        if Y > X:
            print(B * (X - Y) + 2 * C * X)
        else:
            print(max(2 * C * X, 2 * C * Y))


