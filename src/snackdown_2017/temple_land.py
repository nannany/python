R = int(input())
for i in range(R):
    N = int(input())
    strips = list(map(int, input().split()))
    if N % 2 == 0:
        print("no")
        continue

    ans = "yes"
    for j in range(0, N):
        if j <= int(N / 2):
            if strips[j] != j + 1:
                ans = "no"
                break
        else:
            if strips[j] != N - j:
                ans = "no"
                break

    print(ans)
