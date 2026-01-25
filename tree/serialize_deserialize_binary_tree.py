from treenode import TreeNode

def serialize(root):
    res = []
    def dfs(node):
        if not node:
            res.append('#')
            return
        res.append(str(node.data))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(res)

def deserialize(data):
    values = iter(data.split(','))
    def dfs():
        v = next(values)
        if v == '#':
            return None
        node = TreeNode(int(v))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

# Example usage:
# Construct a binary tree:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

#       1
#      / \
#     2   3
#        / \
#       4   5

serialized = serialize(root)
print("Serialized tree:", serialized)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

deserialized_root = deserialize(serialized)
def print_tree(node):
    if not node:
        print('#', end=' ')
        return
    print(node.data, end=' ')
    print_tree(node.left)
    print_tree(node.right)

print("Deserialized tree (preorder):", end=' ')
print_tree(deserialized_root)  # Output: "1 2 # # 3 4 # # 5 # #"