class PrefixSum:
    def __init__(self, nums):
        self.length = len(nums)
        self.prefixes = [0] * self.length
        self.prefixes[0] = nums[0]
        for i in range(1, self.length):
            self.prefixes[i] = self.prefixes[i - 1] + nums[i]

    def sumRange(self, left, right):
        if left <= 0:
            return self.prefixes[right]
        else:
            return self.prefixes[right] - self.prefixes[left - 1]
