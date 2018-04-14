if __name__ == '__main__':
    A, B, X = map(int, input().split())
    if A <= X <= A + B:
        print("YES")
    else:
        print("NO")
