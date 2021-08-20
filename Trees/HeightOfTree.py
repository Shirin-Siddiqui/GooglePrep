class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None


def height(root):
 
    # Base case: empty tree has a height of 0
    if root is None:
        return 0
 
    # recur for the left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Max Height of a Tree - ")
print(height(root))
