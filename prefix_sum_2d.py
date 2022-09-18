class PrefixSum2D:
    def __init__(self, matrix):
        w = len(matrix[0])
        h = len(matrix)
        self.sum2d = [[None] * w for i in range(h)]

        for r in range(h):
            row_sum = 0
            for c in range(w):
                prev_sum = self.sum2d[r - 1][c] if r - 1 >= 0 >= 0 else 0
                row_sum += matrix[r][c]
                self.sum2d[r][c] = prev_sum + row_sum

    def sumRangeZero(self, x, y):
        if x < 0 or y < 0:
            return 0
        else:
            return self.sum2d[y][x]

    def sumRange(self, x1, y1, x2, y2):
        return (self.sumRangeZero(x2, y2) + self.sumRangeZero(x1 - 1, y1 - 1)
                - self.sumRangeZero(x2, y1 - 1) - self.sumRangeZero(x1 - 1, y2))
