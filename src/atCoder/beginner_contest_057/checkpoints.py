N, M = list(map(int, input().split()))

ab = []
for i in range(N):
    ab.append(list(map(int, input().split())))

cd = []
for i in range(M):
    cd.append(list(map(int, input().split())))

for ab_list in ab:
    min_distance = 400000000
    checkpoint = 0
    for cd_list in cd:
        checkpoint += 1
        distance = abs(ab_list[0] - cd_list[0]) + abs(ab_list[1] - cd_list[1])
        if distance < min_distance:
            min_distance = distance
            ans = checkpoint
    print(ans)
