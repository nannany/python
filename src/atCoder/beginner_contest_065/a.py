if __name__ == '__main__':
    X, A, B = list(map(int, input().split()))
    if B - A <= 0:
        print("delicious")
    elif B - A <= X:
        print("safe")
    else:
        print("dangerous")
