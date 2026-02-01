class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    @staticmethod
    def create_bst():
        """
        Creates a binary search tree for testing:
                15
               /  \
              10   20
             / \  / \
            8  12 16 25
        """
        root = TreeNode(15)
        root.left = TreeNode(10)
        root.right = TreeNode(20)
        root.left.left = TreeNode(8)
        root.left.right = TreeNode(12)
        root.right.left = TreeNode(16)
        root.right.right = TreeNode(25)
        return root
    
    @staticmethod
    def create_invalid_bst():
        """
        Creates an invalid binary search tree for testing:
                10
               /  \
              15   5
        """
        root = TreeNode(10)
        root.left = TreeNode(15)
        root.right = TreeNode(5)
        return root
