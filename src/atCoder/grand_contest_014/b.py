N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(M)]

count = [0 for i in range(N)]

# for aibi in ab:
#     ai = aibi[0]
#     bi = aibi[1]
#
#     if bi < ai:
#         tmp = ai
#         ai = bi
#         bi = tmp
#
#     for j in range(ai - 1, bi - 1):
#         count[j] += 1

for aibi in ab:
    ai = aibi[0]
    bi = aibi[1]
    if ai != 1 and bi != 1:
        count[ai - 1] += 1
        count[bi - 1] += 1
    else:
        if ai == 1:
            count[bi - 1] += 1
        else:
            count[ai - 1] += 1

yes_or_no = True
for num in count:
    if num % 2 == 1:
        yes_or_no = False

if yes_or_no:
    print("YES")
else:
    print("NO")
