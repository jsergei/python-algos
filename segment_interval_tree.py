class SegmentIntervalTree:
    def __init__(self, start, end):
        self.storage = {}
        self.start = start
        self.end = end

    def insert_interval(self, ql, qr):
        ql += 1
        qr -= 1
        if ql <= qr:
            self.do_insert(self.start, self.end, ql, qr, 1, 1)

    def do_insert(self, tl, tr, ql, qr, val, i):
        if ql > qr:
            pass
        elif ql == tl and qr == tr:
            self.storage[i] = self.storage.get(i, 0) + val
        else:
            m = (tl + tr) // 2
            self.do_insert(tl, m, ql, min(qr, m), val, 2 * i)
            self.do_insert(m + 1, tr, max(ql, m + 1), qr, val, 2 * i + 1)

    def has_overlap(self, pos):
        tl = self.start
        tr = self.end
        s = 0
        i = 1
        while tl < tr:
            s += self.storage.get(i, 0)
            m = (tl + tr) // 2
            if pos <= m:
                i = i * 2
                tr = m
            else:
                i = i * 2 + 1
                tl = m + 1
        s += self.storage.get(i, 0)
        return s > 0

tree = SegmentIntervalTree(0, 14)
tree.insert_interval(2, 5)
tree.insert_interval(1, 2)
tree.insert_interval(4, 9)
tree.insert_interval(5, 7)
tree.insert_interval(7, 13)

ans = tree.has_overlap(6)
print(ans)