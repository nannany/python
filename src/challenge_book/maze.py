H, W, N = list(map(int, input().split()))
maze = [list(input()) for i in range(H)]

x = -1
for letters in maze:
    x += 1
    y = -1
    for letter in letters:
        y += 1
        if letter == "S":
            sx = x
            sy = y
        elif letter == str(N):
            gx = x
            gy = y

print(sx, sy, gx, gy)
