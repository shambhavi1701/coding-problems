from collections import deque
from treenode import TreeNode

def rightSideView(root):
    if not root:
        return []
    
    q = deque([root])
    result = []

    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == size-1:
                result.append(node.data)
            
    return result


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
result = rightSideView(root)
print("Right side view of the tree:", result)