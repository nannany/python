N, A, B = list(map(int, input().split()))

if B < A:
    print(0)
else:
    max_sum = A + B * (N - 1)
    min_sum = A * (N - 1) + B
    ans = max_sum - min_sum + 1
    if ans < 0:
        print(0)
    else:
        print(ans)
