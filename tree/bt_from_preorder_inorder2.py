from treenode import TreeNode

def buildTree(preorder, inorder):
    index = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def dfs(left, right):
        nonlocal pre_idx
        if left > right:
            return None

        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)

        mid = index[root_val]

        root.left = dfs(left, mid - 1)
        root.right = dfs(mid + 1, right)

        return root

    return dfs(0, len(inorder) - 1)

# Example usage:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder, inorder)
# The constructed binary tree is:
#       3
#      / \
#     9  20
#        /  \
#       15   7

def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.data, end=' ')
        print_inorder(node.right)

print("Inorder traversal of the constructed tree:")
print_inorder(root)  # Output: 9 3 15 20 7
