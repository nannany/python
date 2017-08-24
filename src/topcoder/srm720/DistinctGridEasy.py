class DistinctGridEasy:
    def checkGrid(self, n, k, grid):
        for i in range(0, n):
            tmp_row = grid[n * i:n * (i + 1)]
            if len(set(tmp_row)) != k:
                return "Bad"
            # print(tmp_row)
            tmp_column = []
            for j in range(0, n):
                tmp_column.append(grid[i + (j * n)])

            if len(set(tmp_column)) != k:
                return "Bad"
                # print(tmp_column)
        return "Good"
