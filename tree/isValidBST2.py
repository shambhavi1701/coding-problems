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

# Reset prev for subsequent tests
prev = None
root2 = TreeNode(10)
root2.left = TreeNode(15)
root2.right = TreeNode(5)
result = isValidBST(root2)
print("Is the binary tree a valid BST?", result)  # Output: False