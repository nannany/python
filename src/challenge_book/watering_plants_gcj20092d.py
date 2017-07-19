if __name__ == '__main__':
    T = int(input())
    for caseNo in range(1, T + 1):
        N = int(input())
        X = []
        Y = []
        R = []
        for i in range(N):
            tmp_x, tmp_y, tmp_r = list(map(int, input().split()))
            X.append(tmp_x)
            Y.append(tmp_y)
            R.append(tmp_r)

