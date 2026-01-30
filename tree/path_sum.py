# Path sum in a binary tree
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.

from treenode import TreeNode

def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.data

    return (hasPathSum(root.left, targetSum - root.data) or
            hasPathSum(root.right, targetSum - root.data))

# Time Complexity: O(N), where N is the number of nodes in the tree.
# Space Complexity: O(H), where H is the height of the tree due to recursion stack

# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

targetSum = 22
result = hasPathSum(root, targetSum)
print("Path with sum", targetSum, "exists:", result)  # Output: True

# Another test case
targetSum = 26
result = hasPathSum(root, targetSum)
print("Path with sum", targetSum, "exists:", result)  # Output: True

# Test case where no such path exists
targetSum = 18
result = hasPathSum(root, targetSum)
print("Path with sum", targetSum, "exists:", result)  # Output: False

