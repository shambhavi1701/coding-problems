from treenode import TreeNode

def isValidBST(ROOT):
    def dfs(node, minVal, maxVal):
        if not node:
            return True
        if not (minVal < node.data < maxVal):
            return False
        return (dfs(node.left, minVal, node.data) and
                dfs(node.right, node.data, maxVal))
    return dfs(ROOT, float('-inf'), float('inf'))

root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)

#       15
#      /  \
#    10   20
#    / \  / \
#   8  12 16 25

# Test the function
result = isValidBST(root)
print("Is the binary tree a valid BST?", result)  # Output: True

# Reset for subsequent tests
root2 = TreeNode(10)
root2.left = TreeNode(15)
root2.right = TreeNode(5)
result = isValidBST(root2)
print("Is the binary tree a valid BST?", result)  # Output: False