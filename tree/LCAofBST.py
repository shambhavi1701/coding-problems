from treenode import TreeNode

def lca_of_BST(root, n1, n2):
    curr = root
    while curr:
        if n1 < curr.data and n2 < curr.data:
            curr = curr.left
        elif n1 > curr.data and n2 > curr.data:
            curr = curr.right
        else:
            return curr
    return None

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
result = lca_of_BST(root, 8, 12)
if result:
    print("LCA of 8 and 12 is:", result.data)   
result = lca_of_BST(root, 10, 20)
if result:
    print("LCA of 10 and 20 is:", result.data)
result = lca_of_BST(root, 16, 25)
if result:
    print("LCA of 16 and 25 is:", result.data)
result = lca_of_BST(root, 8, 16)
if result:
    print("LCA of 8 and 16 is:", result.data)