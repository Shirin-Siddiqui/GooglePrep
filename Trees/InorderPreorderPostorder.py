class Node:
    def __init__(self,key):
        self.left = None
        self.val = key
        self.right = None

#      1
#    /   \
#   2     3
#  / \   
# 4   5 

# InOrder -> Left , Root , Right
# PreOrder -> Root , Left , Right
# PostOrder -> Left , Right , Root

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)

def printPreOrder(root):
    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

print("Inorder Traversal --> ")
printInOrder(root)

print("\nPreorder Traversal --> ")
printPreOrder(root)

print("\nPostorder Traversal --> ")
printPostOrder(root)

