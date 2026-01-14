
from treenode import TreeNode

def dfs(root):
    if root is None:
        return 0
    
    left = dfs(root.left)
    right = dfs(root.right)

    return 1+max(left, right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#       1
#      / \
#     2   3
#    / \  \
#   4  5

result = dfs(root)
print("Maximum depth of the tree:", result)  # Output: 3