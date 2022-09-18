import itertools

class PrefixSum:
    def __init__(self, nums):
        self.n = len(nums)
        self.prefix = list(itertools.accumulate(nums))
        self.dprefix = list(itertools.accumulate(self.prefix))

    def sum_range_to_right(self, s, e):
        if s <= 0:
            return self.dprefix[e]
        if e >= self.n:
            e = self.n - 1
        if s > e:
            return 0
        return self.dprefix[e] - self.dprefix[s - 1] - (e - s + 1) * self.prefix[s - 1]

    def sum_range_to_left(self, s, e):
        if s <= 0:
            return self.sum_range_base(0, e) * (e + 2) - self.dprefix[e]
        if e >= self.n:
            e = self.n - 1
        if s > e:
            return 0
        return self.sum_range_base(s, e) * (e - s + 2) - self.dprefix[e] + self.dprefix[s - 1] + (e - s + 1) * \
               self.prefix[s - 1]

    def sum_range_base(self, s, e):
        if s <= 0:
            return self.prefix[e]
        if e >= self.n:
            e = self.n - 1
        if s > e:
            return 0
        return self.prefix[e] - self.prefix[s - 1]

p = PrefixSum([1,2,3,4])

r = p.sum_range_to_left(1, 3)
print(r)