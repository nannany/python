A, B, K = map(int, input().split())

ans = []
for i in range(K):
    if A + i <= B:
        ans.append(A + i)
    else:
        break

for j in range(K):
    if B - j >= A:
        ans.append(B - j)
    else:
        break

ans2 = sorted(list(set(ans)))

for a in ans2:
    print(a)
