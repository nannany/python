from operator import itemgetter

if __name__ == '__main__':
    N = int(input())
    plots = []
    for i in range(2 * N):
        x, y = map(int, input().split())
        if i < N:
            plots.append([x, y, "r"])
        else:
            plots.append([x, y, "b"])

    plots = sorted(plots, key=itemgetter(0))

    t_set = set()
    ans = 0
    for x, y, c in plots:
        if c == "r":
            t_set.add(y)
            continue

        if len(t_set) == 0 or y < min(t_set):
            continue

        ans += 1
        del_y = 0
        for tmp in t_set:
            if y > tmp > del_y:
                del_y = tmp

        t_set.remove(del_y)

    print(ans)
