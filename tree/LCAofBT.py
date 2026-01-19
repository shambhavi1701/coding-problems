from treenode import TreeNode

def lca(root,n1,n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left = lca(root.left,n1,n2)
    right = lca(root.right,n1,n2)

    if left and right:
        return root
    
    return left if left else right


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
result = lca(root,8,12)
if result:
    print("LCA of 8 and 12 is:", result.data)

result = lca(root,8,16)
if result:
    print("LCA of 8 and 16 is:", result.data)