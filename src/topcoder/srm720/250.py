import DistinctGridEasy;

if __name__ == '__main__':
    tes = DistinctGridEasy.DistinctGridEasy()
    n = int(input())
    k = int(input())
    grid = list(input().split())
    print(grid)
    print(tes.checkGrid(n, k, grid))
