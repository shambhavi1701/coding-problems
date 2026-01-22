from treenode import TreeNode

def kthSmallestElement(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.data
            return
        inorder(node.right)
    inorder(root)
    return result


# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)

#       5
#      / \
#     3   7
#    / \  /
#   2  4 6

k = 3
result = kthSmallestElement(root, k)
print(f"The {k}th smallest element in the BST is:", result)  # Output: 4

k = 5
result = kthSmallestElement(root, k)
print(f"The {k}th smallest element in the BST is:", result)  # Output: 6