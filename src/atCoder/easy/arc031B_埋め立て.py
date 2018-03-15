from collections import deque
import copy


def check(tmp_tizu, tmp_judge):
    for i in range(10):
        for j in range(10):
            if tmp_tizu[i][j] == "o" and not tmp_judge[i][j]:
                return False

    return True


dif = [[-1, 0], [1, 0], [0, -1], [0, 1]]

if __name__ == '__main__':
    tizu = [list(input()) for _ in range(10)]
    judge = [[False for _ in range(10)] for __ in range(10)]
    for i in range(10):
        for j in range(10):
            if tizu[i][j] == "o":
                continue

            tmp_tizu = copy.deepcopy(tizu)
            tmp_tizu[i][j] = "o"
            tmp_judge = copy.deepcopy(judge)
            tmp_judge[i][j] = True
            q = deque()
            q.append([i, j])

            while len(q) != 0:
                y, x = q.pop()
                tmp_judge[y][x] = True
                for dy, dx in dif:
                    if 0 <= y + dy < 10 and 0 <= x + dx < 10:
                        if tmp_tizu[y + dy][x + dx] == "o" and not tmp_judge[y + dy][x + dx]:
                            q.append([y + dy, x + dx])

            if check(tmp_tizu, tmp_judge):
                print("YES")
                exit()
            else:
                continue

    print("NO")
