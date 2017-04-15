# N:ありの頭数　L:周の長さ　T:時間。この時の状態を求める
N, L, T = list(map(int, input().split()))

ant = [list(map(int, input().split())) for i in range(N)]

line_pos = []
for i in range(0, N):
    if ant[i][1] == 1:
        line_pos.append(ant[i][0] + T)
    else:
        line_pos.append(ant[i][0] - T)
# X1についてのみみる
if ant[0][1] == 1:
    crash_count = 0
    for i in range(1, N):
        if ant[i][1] == 2:
            crash_count += (2 * T - ant[i][0] + ant[0][0]) // L + 1
else:
    crash_count = 0
    for i in range(1, N):
        if ant[i][1] == 1:
            crash_count += (2 * T - ant[i][0] + ant[0][0]) // L + 1
ans_pos = [-1 for i in range(N)]
if ant[0][1] == 1:
    for i in range(0, N):
        if crash_count + i < N:
            ans_pos[crash_count + i] = line_pos[i] % L
        else:
            ans_pos[crash_count + i - N] = line_pos[i] % L
else:
    for i in range(0, N):
        if 0 < i - crash_count:
            ans_pos[N - (i - crash_count)] = line_pos[i] % L
        else:
            ans_pos[i - crash_count] = line_pos[i] % L

for ans in ans_pos:
    print(ans)
