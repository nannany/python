import copy


def get_min_x():
    min_x = float('inf')
    for x, y, i in plots:
        if x < min_x:
            ret = (x, y, i)
    return ret


def get_max_x():
    max_x = -float('inf')
    for x, y, i in plots:
        if x > max_x:
            ret = (x, y, i)
    return ret


def get_min_y():
    min_y = float('inf')
    for x, y, i in plots:
        if y < min_y:
            ret = (x, y, i)
    return ret


def get_max_y():
    max_y = -float('inf')
    for x, y, i in plots:
        if y > max_y:
            ret = (x, y, i)
    return ret


def get_in_num():
    ret = 0
    for x, y, i in org_plots:
        if min_x[0] <= x <= max_x[0] and min_y[1] <= y <= max_y[1]:
            ret += 1
    return ret

if __name__ == '__main__':
    N, K = map(int, input().split())
    plots = []
    for i in range(N):
        tmp_x, tmp_y = map(int, input().split())
        plots.append((tmp_x, tmp_y, i))
    org_plots = copy.deepcopy(plots)
    min_x = get_min_x(plots)
    max_x = get_max_x(plots)
    min_y = get_min_y(plots)
    max_y = get_max_y(plots)

    x_leng = max_x - min_x
    y_leng = max_y - min_y

    while True:
