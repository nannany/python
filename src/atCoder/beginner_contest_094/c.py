if __name__ == '__main__':
    N = int(input())
    X = list(map(int, input().split()))
    X_sorted = sorted(X)

    cand1 = X_sorted[N // 2 - 1]
    cand2 = X_sorted[N // 2]

    for target in X:
        if cand1 >= target:
            print(cand2)
        else:
            print(cand1)

