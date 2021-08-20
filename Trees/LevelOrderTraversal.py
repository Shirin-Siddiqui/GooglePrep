class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

# Algorithm - 
# if queue is none then return
# 1) create a queue and fill root element
# 2) length of queue is greater than 0
#       print the val at 0th position of the queue
#       pop the value from the queue
#       fill left and right childs if exists


def levelOrderTraversal(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].val)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Level Order Traversal of Tree - ")
levelOrderTraversal(root)

