class SegmentMergeTree:
    def __init__(self, nums):
        self.length = len(nums)
        self.tree = [None] * (self.length * 4)
        self.set_level(0, self.length - 1, 1, nums)

    def set_level(self, tl, tr, i, nums):
        if tl > tr:
            return []
        elif tl == tr:
            self.tree[i] = [nums[tl]]
            return self.tree[i]
        else:
            m = (tl + tr) // 2
            left_arr = self.set_level(tl, m, i * 2, nums)
            right_arr = self.set_level(m + 1, tr, i * 2 + 1, nums)
            self.tree[i] = self.merge(left_arr, right_arr)
            return self.tree[i]

    def find_max_less(self, x, ql, qr):
        return self.do_find_max_less(x, 0, self.length - 1, ql, qr, 1)

    def do_find_max_less(self, x, tl, tr, ql, qr, i):
        if ql > qr:
            return float('-inf')
        elif ql == tl and qr == tr:
            return self.find_val_binary(self.tree[i], x, 0, len(self.tree[i]) - 1)
        else:
            m = (tl + tr) // 2
            left_tree = self.do_find_max_less(x, tl, m, ql, min(qr, m), 2 * i)
            right_tree = self.do_find_max_less(x, m + 1, tr, max(ql, m + 1), qr, 2 * i + 1)
            return max(left_tree, right_tree)

    def merge(self, a, b):
        ai = bi = ri = 0
        res = [0] * (len(a) + len(b))
        while ai < len(a) and bi < len(b):
            if a[ai] <= b[bi]:
                res[ri] = a[ai]
                ai += 1
            else:
                res[ri] = b[bi]
                bi += 1
            ri += 1
        while ai < len(a):
            res[ri] = a[ai]
            ai += 1
            ri += 1
        while bi < len(b):
            res[ri] = b[bi]
            bi += 1
            ri += 1
        return res

    def find_val_binary(self, arr, query, left, right):
        if left == right:
            return arr[left] if arr[left] < query else float('-inf')
        else:
            m = (left + right) // 2
            if arr[m] < query:
                right_arr = self.find_val_binary(arr, query, m + 1, right)
                return max(arr[m], right_arr)
            else:
                return self.find_val_binary(arr, query, left, max(left, m - 1))


tree = SegmentMergeTree([2, 7, 1, 8, 4, 5, -1, 9])
ans = tree.find_max_less(2, 4, 4)
print(ans)
