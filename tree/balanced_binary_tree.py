from treenode import TreeNode

def isBalanced(node):
    def dfs(root):
        if root is None:
            return [True, 0]
        left = dfs(root.left)
        right = dfs(root.right)

        balanced = left[0] and right[0] and (abs(left[1]-right[1])<=1)
        return [balanced, 1+max(left[1],right[1])]
    return dfs(node)[0]

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)

#       1
#      / \
#     2   3
#    / \
#   4   5
#  / \
# 6   7

result = isBalanced(root)
print("Is the binary tree balanced?", result)  # Output: False