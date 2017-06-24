if __name__ == '__main__':
    N = int(input())
    x = []
    y = []
    for i in range(N):
        tmp_x, tmp_y = list(map(int, input().split()))
        x.append(tmp_x)
        y.append(tmp_y)

    x_0 = x[0]
    y_0 = y[0]
    x = [ele - x_0 for ele in x]
    y = [ele - y_0 for ele in y]
    print(x)
    print(y)

    solve_list = [min(ele_x, ele_y) for ele_x in x for ele_y in y]
    print(solve_list)
