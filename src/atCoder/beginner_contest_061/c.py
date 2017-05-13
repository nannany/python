def C(_mid):
    tmp_sum = 0
    if len(ab) <= _mid:
        return False
    for i in range(0, _mid):
        tmp_sum += ab[i][1]
    if tmp_sum < K:
        return True
    else:
        return False


N, K = list(map(int, input().split()))
ab = []
for i in range(N):
    a, b = list(map(int, input().split()))
    ab.append([a, b])

ab.sort(key=lambda x: x[0])

lb = 0
ub = 100000
while ub - lb > 1:
    # print(str(lb) + " " + str(ub))
    mid = int((lb + ub) / 2)
    if C(mid):
        lb = mid
    else:
        ub = mid

print(ab[lb][0])
