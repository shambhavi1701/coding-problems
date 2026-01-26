from treenode import TreeNode

def isSameTree(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.data != q.data:
        return False

    return (isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))

# Example usage:
# Construct first binary tree:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
#       1
#      / \
#     2   3
# Construct second binary tree:
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
#       1
#      / \
#     2   3

result = isSameTree(root1, root2)
print("Are the two binary trees identical?", result)  # Output: True