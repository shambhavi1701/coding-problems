from treenode import TreeNode

def lca_of_bst(root, n1, n2):
    curr = root
    while curr:
        if n1 < curr.data and n2 < curr.data:
            curr = curr.left
        elif n1 > curr.data and n2 > curr.data:
            curr = curr.right
        else:
            return curr
    return None

root = TreeNode.create_bst()
"""
Creates a binary search tree for testing:
                15
               /  \
              10   20
             / \  / \
            8  12 16 25
"""


# Test the function
result = lca_of_bst(root, 8, 12)
if result:
    print("LCA of 8 and 12 is:", result.data)   # Expected LCA is 10
result = lca_of_bst(root, 10, 20)
if result:
    print("LCA of 10 and 20 is:", result.data)  # Expected LCA is 15
result = lca_of_bst(root, 16, 25)
if result:
    print("LCA of 16 and 25 is:", result.data)  # Expected LCA is 20
result = lca_of_bst(root, 8, 16)
if result:
    print("LCA of 8 and 16 is:", result.data)   # Expected LCA is 15