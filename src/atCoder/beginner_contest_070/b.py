if __name__ == '__main__':
    A, B, C, D = list(map(int, input().split()))
    if B <= C:
        print(0)
    elif B <= D:
        if A <= C:
            print(B - C)
        else:
            print(B - A)
    else:
        if A <= C:
            print(D - C)
        elif A <= D:
            print(D - A)
        else:
            print(0)
