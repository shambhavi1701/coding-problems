from treenode import TreeNode

def isSymmetric(root):
    def mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.data != t2.data:
            return False

        return (mirror(t1.left, t2.right) and
                mirror(t1.right, t2.left))

    return mirror(root.left, root.right)

# Example usage:
# Construct a symmetric binary tree:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3

result = isSymmetric(root)
print("Is the binary tree symmetric?", result)  # Output: True