def dfs(i, b, c):
    if i == 10:
        b_sort = sorted(b)
        c_sort = sorted(c)
        return (b == b_sort and c == c_sort)

    if dfs(i + 1, b + [balls[i - 1]], c):
        return True

    if dfs(i + 1, b, c + [balls[i - 1]]):
        return True

    return False


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        balls = list(map(int, input().split()))
        if dfs(1, [0], [0]):
            print("YES")
        else:
            print("NO")
