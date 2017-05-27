S = list(input())

ans = 0
for i in range(0, len(S)):
    if S[i] == 'U':
        ans += ((len(S) - 1) - i) + i * 2
    else:
        ans += ((len(S) - 1) - i) * 2 + i

print(ans)
