from treenode import TreeNode

def flatten(root):
    prev = None

    def dfs(node):
        nonlocal prev
        if not node:
            return

        dfs(node.right)
        dfs(node.left)

        node.right = prev
        node.left = None
        prev = node

    dfs(root)

# Example usage:
# Construct a binary tree:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
#       1
#      / \
#     2   5
#    / \   \
#   3   4   6

flatten(root)
# Print the flattened linked list:
current = root
while current:
    print(current.data, end=' ')
    current = current.right
# Output: 1 2 3 4 5 6