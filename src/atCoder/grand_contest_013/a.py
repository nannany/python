N = int(input())
a = list(map(int, input().split()))

# 0:未定 1:増加　-1:減少
status = 0
ans = 1
for i in range(1, N):
    if status == 0:
        if a[i - 1] < a[i]:
            status = 1
        elif a[i] < a[i - 1]:
            status = -1
    elif status == 1:
        if a[i] < a[i - 1]:
            status = 0
            ans += 1
    elif status == -1:
        if a[i - 1] < a[i]:
            status = 0
            ans += 1

print(ans)
