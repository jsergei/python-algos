# SPARSE TABLE
import math

class SparseTable:
    # used for overlapping friendly sequences, such as min(a,b), max(a,b), gcd(a,b)
    def __init__(self, nums, func):
        self.func = func
        self.build_table(nums)

    def build_table(self, nums):
        self.width = len(nums)
        self.height = math.floor(math.log2(self.width)) + 1

        self.table = [nums[:]]
        self.table[1:] = [[None] * self.width for r in range(1, self.height)]

        int_size = 2
        for row in range(1, self.height):
            half_int = int_size // 2
            for col in range(0, self.width - int_size):
                self.table[row][col] = self.func(self.table[row - 1][col], self.table[row - 1][col + half_int])
            int_size *= 2

    # [start, end] interval
    def get_value(self, start, end):
        start = max(0, start)
        end = min(self.width - 1, end)
        int_size_pow = math.floor(math.log2(end - start + 1))
        return self.func(self.table[int_size_pow][start], self.table[int_size_pow][end - 2 ** int_size_pow])
