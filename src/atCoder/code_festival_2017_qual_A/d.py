from collections import deque

colors = ["R", "B", "Y", "G"]

if __name__ == '__main__':
    H, W, d = list(map(int, input().split()))

    que = deque()

    possibility = [[[] for i in range(W)] for j in range(H)]
    searched = [[False for i in range(W)] for j in range(H)]

    # (0,0) は赤で考える
    possibility[0][0].extend(["B", "Y", "G"])
    searched[0][0] = True
    print(possibility)
    print(searched)
    for i in range(0, d + 1):
        if 0 <= i <= W - 1 and 0 <= d - i <= H - 1:
            que.append((i, d - i, "R"))

    while len(que) != 0:
        tmp_h, tmp_w, color = que.popleft()
        if searched[tmp_h][tmp_w]:
            continue

        possibility[tmp_h][tmp_w].append(color)
        searched[tmp_h][tmp_w] = True

        for i in range(-d, d + 1):
            que.append()
