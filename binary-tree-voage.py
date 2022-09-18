class TreeNode:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

#       1
#   2      3
# 4   5  6

voage = [1, 3, 6, 2, 5, 4]

children = {}
def collect_children(node):
    children[node.val] = []
    if node.left:
        children[node.val].append(node.left.val)
    if node.right:
        children[node.val].append(node.right.val)

flips = 0
def visit_voage(i, voage, n):
    left_i = i * 2 + 1
    right_i = (i + 1) * 2
    o_left, o_right = children[voage[i]]
    if left_i < n and right_i < n:
        if o_left and o_right:
            if voage[left_i] == o_left and voage[right_i] == o_right:
                # same order
                return visit_voage(left_i, voage, n) + visit_voage(right_i, voage, n)
            elif voage[left_i] == o_right and voage[right_i] == o_left:
                # reverse order
                return 1 + visit_voage(left_i, voage, n) + visit_voage(right_i, voage, n)
            else:
                return -1 # numbers are different
        else:
            return -1
    elif left_i < n:
        if o_left and o_right:
            return -1
        elif o_left:
            if voage[left_i] == o_left:
                # same order
                return visit_voage(left_i, voage, n)
            else:
                return -1
        elif o_right:
            if voage[left_i] == o_right:
                # reverse order
                return 1 + visit_voage(left_i, voage, n)
            else:
                return -1
        else:
            return -1
    elif right_i < n:
        if o_left and o_right:
            return -1
        elif o_left:
            if voage[right_i] == o_left:
                # reverse order
                return 1 + visit_voage(right_i, voage, n)
            else:
                return -1
        elif o_right:
            if voage[right_i] == o_right:
                # same order
                return visit_voage(right_i, voage, n)
            else:
                return -1
        else:
            return -1
    else:
        return -1
