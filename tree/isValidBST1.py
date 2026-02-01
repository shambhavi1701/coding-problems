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

# Test the function with a valid BST
root = TreeNode.create_bst()
result = isValidBST(root)
print("Is the binary tree a valid BST?", result)  # Output: True

# Test with an invalid BST
root2 = TreeNode.create_invalid_bst()
result = isValidBST(root2)
print("Is the binary tree a valid BST?", result)  # Output: False