class NumArray:
    def __init__(self, nums):
        self.length = len(nums)
        self.tree = [0] * self.length
        for i in range(self.length):
            self.updateTree(i, nums[i])

    def update(self, index, new_val):
        old_value = self.sumRange(index, index)
        self.updateTree(index, new_val - old_value)

    def updateTree(self, index, delta):
        j = index
        while j < self.length:
            self.tree[j] += delta
            j = (j + 1) | j

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left - 1)

    def prefixSum(self, right):
        s = 0
        j = right
        while j >= 0:
            s += self.tree[j]
            j = (j & (j + 1)) - 1
        return s