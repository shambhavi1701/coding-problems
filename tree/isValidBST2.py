from treenode import TreeNode

prev = None
def isValidBST(root):
    global prev
    if root is None:
        return True
    if not isValidBST(root.left):
        return False
    if prev is not None and root.data <= prev.data:
        return False
    prev = root
    return isValidBST(root.right)

# Test the function with a valid BST
root = TreeNode.create_bst()
result = isValidBST(root)
print("Is the binary tree a valid BST?", result)  # Output: True

# Reset prev for subsequent tests
prev = None
root2 = TreeNode.create_invalid_bst()
result = isValidBST(root2)
print("Is the binary tree a valid BST?", result)  # Output: False