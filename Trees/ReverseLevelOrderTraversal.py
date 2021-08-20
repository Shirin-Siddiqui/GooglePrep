from collections import deque
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

'''
1) We initialize a q and a stack  and put root in it
2) while loop through q until 0 elements left
    pop from queue and append in stack 
    check if right child present insert in queue
    check if left child presenr insert in queue
'''


def reverseLevelOrderTraversal(root):
    queue = deque()
    queue.append(root)
    stack = deque()
    while queue:
        node = queue.popleft()
        stack.appendleft(node.val)
        
        if node.right is not None:
            queue.append(node.right)
        
        if node.left is not None:
            queue.append(node.left)
    
    return stack



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Reverse Order Tree Traversal - ")
print (reverseLevelOrderTraversal(root))

