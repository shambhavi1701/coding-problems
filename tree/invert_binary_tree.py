from treenode import TreeNode

def print_tree(root):
    if root is None:
        return
    print(root.data, end=' ')
    print_tree(root.left)
    print_tree(root.right)

def invertTree(root):
    if not root:
        return None
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root

# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original binary tree (pre-order):")
print_tree(root)  # Output: 4 2 1 3 7 6 9
print("\n")
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

inverted_root = invertTree(root)

# The inverted tree should be:
#       4
#      / \
#     7   2
#    / \ / \
#   9  6 3  1

print("Inverted binary tree (pre-order):")
print_tree(inverted_root)  # Output: 4 7 9 6 2 3 1