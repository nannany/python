n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sum_x = 0
for i in range(0, n):
    tmp_x = x[i]
    sum_x += sum(list(filter(lambda ele: ele > 0, (map(lambda ele: ele - tmp_x, x)))))

sum_y = 0
for i in range(0, m):
    tmp_y = y[i]
    sum_y += sum(list(filter(lambda ele: ele > 0, (map(lambda ele: ele - tmp_y, y)))))

ans = sum_x * sum_y

divide_num = pow(10, 9) + 7
print(ans % divide_num)
