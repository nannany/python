if __name__ == '__main__':
    N = int(input())
    x = []
    y = []
    for i in range(N):
        tmp_x, tmp_y = list(map(int, input().split()))
        xy_list = [list(map(int, input().split())) for _ in range(N)]
