from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxEachLevel(root):
    if not root:
        return []
    
    q = deque([root])
    result = []

    while q:
        maximum = float('-inf')
        for i in range(len(q)):
            node = q.popleft()
            maximum = max(maximum, node.data)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        result.append(maximum)
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
result = maxEachLevel(root)
print("Maximum value at each level:", result)