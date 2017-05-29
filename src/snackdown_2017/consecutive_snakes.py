import math

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, L, A, B = list(map(int, input().split()))
        S = list(map(int, input().split()))
        S.sort()

        ave = sum(S) / len(S)
        # 切り上げ
        ceil_lower_limit = round(ave) - math.ceil(N * L / 2)
        ceil_upper_limit = round(ave) + math.floor(N * L / 2)

        if ceil_lower_limit < A:
            ceil_upper_limit += A - ceil_lower_limit
            ceil_lower_limit = A

        if B < ceil_upper_limit:
            ceil_lower_limit -= ceil_upper_limit - B
            ceil_upper_limit = B

        print(ceil_lower_limit)
        print(ceil_upper_limit)

        ceil_ans = 0
        for j in range(0, N):
            ceil_ans += abs((ceil_lower_limit + L * j) - S[j])

        print(int(ceil_ans))
        print("★")
        # 切り下げ
        floor_lower_limit = round(ave) - math.floor(N * L / 2)
        floor_upper_limit = round(ave) + math.ceil(N * L / 2)

        if floor_lower_limit < A:
            floor_upper_limit += A - floor_lower_limit
            floor_lower_limit = A

        if B < floor_upper_limit:
            floor_lower_limit -= floor_upper_limit - B
            floor_upper_limit = B

        print(floor_lower_limit)
        print(floor_upper_limit)

        floor_ans = 0
        for j in range(0, N):
            floor_ans += abs((floor_lower_limit + L * j) - S[j])

        print(int(floor_ans))

        if floor_ans < ceil_ans:
            print(floor_ans)
        else:
            print(ceil_ans)
