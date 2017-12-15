if __name__ == '__main__':
    A, B = map(int, input().split())
    S = input()
    if A <= len(S) <=B:
        print('YES')
    else:
        print('NO')
