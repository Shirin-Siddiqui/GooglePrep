# Recursive Solution - 

# AVERAGE COMPLEXITY -------------
# Time Complexity - O(log(n))
# Space Complexity - O(log(n))

# WORST COMPLEXITY -------------
# Time Complexity - O(n)
# Space Complexity - O(n)

def findClosestValueInBstR(tree, target):
    return findClosestValueInBstHelperR(tree, target, tree.value)

def findClosestValueInBstHelperR(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelperR(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelperR(tree.right, target, closest)
    else:
        return closest


# Iterative Solution - 

# AVERAGE COMPLEXITY -------------
# Time Complexity - O(log(n))
# Space Complexity - O(1)

# WORST COMPLEXITY -------------
# Time Complexity - O(n)
# Space Complexity - O(1)

def findClosestValueInBstI(tree, target):
    return findClosestValueInBstHelperI(tree, target, tree.value)

def findClosestValueInBstHelperI(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)
root.right.left.right = BST(14)

closestValue = findClosestValueInBstI(root, 12)
print("The closest value is: " + str(closestValue))

