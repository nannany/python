import itertools
import copy

if __name__ == '__main__':
    N, K = map(int, input().split())
    plots = []
    for i in range(N):
        tmp_x, tmp_y = map(int, input().split())
        plots.append((tmp_x, tmp_y))
    combi_x = list(itertools.combinations(plots, 2))
    combi_y = list(itertools.combinations(plots, 2))
    menseki = float('inf')
    for x1, x2 in combi_x:
        for y1, y2 in combi_y:
            left_x = min(x1[0], x2[0], y1[0], y2[0])
            right_x = max(x1[0], x2[0], y1[0], y2[0])
            bottom_y = min(x1[1], x2[1], y1[1], y2[1])
            top_y = max(x1[1], x2[1], y1[1], y2[1])
            in_num = 0
            for x, y in plots:
                if left_x <= x <= right_x and bottom_y <= y <= top_y:
                    in_num += 1

            if K <= in_num:
                if (right_x - left_x) * (top_y - bottom_y) < menseki:
                    menseki = (right_x - left_x) * (top_y - bottom_y)

    print(menseki)
