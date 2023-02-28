from collections import namedtuple


def count(node):
    if not node.left and not node.right: return 0
    left = count(node.left) if node.left is not None else 0
    right = count(node.right) if node.right is not None else 0
    return left + right

    
if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8
    print(count(Node(left=None, right=None))) # 0
    print(count(Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))) # 2