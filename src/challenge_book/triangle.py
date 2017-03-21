n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

maxLen = 0

for i in range(0, len(a) - 2):
    breakFlag = 0
    for j in range(i + 1, len(a) - 1):
        if breakFlag == 1: break
        for k in range(j + 1, len(a)):
            if a[i] < a[j] + a[k]:
                if maxLen < a[i] + a[j] + a[k]:
                    maxLen = a[i] + a[j] + a[k]
                    breakFlag = 1
                    break
                else:
                    breakFlag = 1
                    break

print(maxLen)
