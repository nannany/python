import math

if __name__ == '__main__':
    N, S, T = list(map(int, input().split()))
    S_pos = int(math.log(S, 2))
    # print(S_pos)
    ans = 0
    lb = S
    ub = S
    for i in range(N - S_pos):
        if lb <= T <= ub:
            ans = i
            break
        elif T < lb:
            ans = -1
            break
        else:
            ub = ub * 2 + 1
            lb = lb * 2

    print(ans)
