N, A, B = list(map(int, input().split()))

v = list(map(int, input().split()))

v.sort(reverse=True)

sum_val = 0
for i in range(0, A):
    sum_val += v[i]

max_ave = sum_val / A

count = 0
for i in range(A, B):
    for j in range(0, i - 1):
        tmp_sum = v[j]
