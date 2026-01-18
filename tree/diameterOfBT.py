from treenode import TreeNode

def diameter_of_BT(root):
    diameter = 0
    def dfs(root):
        nonlocal diameter
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter, left+right)
        return 1+max(left, right)
    dfs(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#       1
#      / \
#     2   3
#    / \
#   4   5

result = diameter_of_BT(root)
print("Diameter of the binary tree:", result)  # Output: 3