from collections import deque
from treenode import TreeNode

def avgEachLevel(root):
    if not root:
        return []
    
    result = []
    q = deque([root])

    while q:
        size = len(q)
        total = 0
        for  i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            total += node.data
        result.append(total/size)
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
result = avgEachLevel(root)
print("Average value at each level:", result)


