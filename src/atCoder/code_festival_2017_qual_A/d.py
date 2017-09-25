colors = ["R", "B", "Y", "G"]

if __name__ == '__main__':
    H, W, d = list(map(int, input().split()))

    ans = [["" for j in range(W)] for i in range(H)]
    for i in range(0, H):
        for j in range(0, W):
            # 45度変換後の値、x,y
            x = i - j
            y = i + j

            if 1 <= x % (2 * d) <= d:
                if 1 <= y % (2 * d) <= d:
                    ans[i][j] = "R"
                else:
                    ans[i][j] = "B"
            else:
                if 1 <= y % (2 * d) <= d:
                    ans[i][j] = "Y"
                else:
                    ans[i][j] = "G"

    for tmpans in ans:
        print("".join(tmpans))
