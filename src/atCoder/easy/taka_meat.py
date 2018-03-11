if __name__ == '__main__':
    N = int(input())
    t = [int(input()) for _ in range(N)]

    recur_num = 2 ** N

    ans = float('inf')
    for i in range(recur_num):
        tmp1 = 0
        tmp2 = 0
        for j in range(N):
            if i & 2 ** j:
                tmp1 += t[j]
            else:
                tmp2 += t[j]

        if max(tmp1,tmp2) < ans:
            ans = max(tmp1,tmp2)

    print(ans)