N, M, Q = list(map(int, input().split()))
S = [list(map(int, list(input()))) for i in range(N)]

accum_sum_black = []
accum_sum_edge_x = []
accum_sum_edge_y = []
for i in range(0, N):
    adding = 0
    for j in range(0, M):
        if S[i][j] == 1:
            adding += 1
            accum_sum_black.append(adding)
        else:
            accum_sum_black.append(adding)

for i in range(0, N):
    adding = 0
    before = False
    for j in range(0, M):
        if before and S[i][j] == 1:
            adding += 1
            accum_sum_edge_x.append(adding)
        elif S[i][j] == 1:
            accum_sum_edge_x.append(adding)
            before = True
        else:
            accum_sum_edge_x.append(adding)
            before = False

for j in range(0, M):
    adding = 0
    before = False
    for i in range(0, N):
        if before and S[i][j] == 1:
            adding += 1
            accum_sum_edge_y.append(adding)
        elif S[i][j] == 1:
            accum_sum_edge_y.append(adding)
            before = True
        else:
            accum_sum_edge_y.append(adding)
            before = False

for i in range(Q):
    x1, y1, x2, y2 = list(map(int, input().split()))
    sum_of_black = 0
