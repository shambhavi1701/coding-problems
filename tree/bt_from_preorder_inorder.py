from treenode import TreeNode

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # first preorder element is root
    root = TreeNode(preorder[0])

    # find root in inorder
    mid = inorder.index(preorder[0])

    # build left and right subtrees
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

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