from collections import namedtuple

def count(node, counter=0):
    right = 0
    left = 0
    if node.left == None and node.right == None:
        counter +=1
    if node.left != None:
        left = count(node.left, counter)
    if node.right != None:
        right = count(node.right, counter)
    return counter + right + left

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2