import math

class NumArray:

    def __init__(self, nums):
        min_2n_size = 2 ** math.ceil(math.log2(len(nums)))
        self.original_len = len(nums)
        self.segments = [0] * (min_2n_size * 2 - 1)
        self.build_tree(0, len(nums) - 1, 0, nums)

    def build_tree(self, range_s, range_e, index, nums):
        if range_s == range_e:
            self.segments[index] = nums[range_s]
            return self.segments[index]
        else:
            mid = self.get_mid_range(range_s, range_e)
            left = self.build_tree(range_s, mid, self.get_lchild(index), nums)
            right = self.build_tree(mid + 1, range_e, self.get_rchild(index), nums)
            self.segments[index] = left + right
            return self.segments[index]

    def get_lchild(self, index):
        return index * 2 + 1

    def get_rchild(self, index):
        return index * 2 + 2

    def get_parent(self, index):
        return (index - 1) // 2

    def is_subset_overlap(self, parent_s, parent_e, child_s, child_e):
        return not (child_s > parent_e or child_e < parent_s)

    def is_proper_subset(self, parent_s, parent_e, child_s, child_e):
        return child_s >= parent_s and child_e <= parent_e

    def get_mid_range(self, range_s, range_e):
        return range_s + (range_e - range_s) // 2

    def update(self, index, val):
        internal_i = self.find_internal_i(index, 0, 0, self.original_len - 1)
        if internal_i == -1:
            return -1
        self.segments[internal_i] = val
        p = internal_i
        while p != 0:
            parent = self.get_parent(p)
            self.segments[parent] = self.segments[self.get_lchild(parent)] + self.segments[
                self.get_rchild(parent)]
            p = parent

    def find_internal_i(self, search_i, internal_i, range_s, range_e):
        if range_s == range_e:
            return internal_i if search_i == range_s else -1
        else:
            mid = self.get_mid_range(range_s, range_e)
            if self.is_proper_subset(range_s, mid, search_i, search_i):
                return self.find_internal_i(search_i, self.get_lchild(internal_i), range_s, mid)
            elif self.is_proper_subset(mid + 1, range_e, search_i, search_i):
                return self.find_internal_i(search_i, self.get_rchild(internal_i), mid + 1, range_e)
            else:
                return -1

    def sumRange(self, left: int, right: int) -> int:
        return self.calc_sum_range(0, self.original_len - 1, left, right, 0)

    def calc_sum_range(self, tree_range_s, tree_range_e, search_range_s, search_range_e, index):
        if self.is_subset_overlap(search_range_s, search_range_e, tree_range_s, tree_range_e):
            if self.is_proper_subset(search_range_s, search_range_e, tree_range_s, tree_range_e):
                return self.segments[index]
            else:
                mid = self.get_mid_range(tree_range_s, tree_range_e)
                left = self.calc_sum_range(tree_range_s, mid, search_range_s, search_range_e,
                                           self.get_lchild(index))
                right = self.calc_sum_range(mid + 1, tree_range_e, search_range_s, search_range_e,
                                            self.get_rchild(index))
                return left + right
        else:
            return 0

