from collections import namedtuple

class MyNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.visited = False

def count(node):
    d = {}
    n = make_structure(node)
    while True:
        if n.right:
            print(n.right.val)
            n = n.right
        if n.left:
            print(n.left.val)
            # n = n.left
        else:
            break
    print(n.val)

def get_leaves(node, d, lvl=0):
    if not node:
        return
    if not node.left and not node.right:
        d[lvl] = 1 if lvl not in d.keys() else d[lvl] + 1
    if node.left:
        get_leaves(node.left, d, lvl+1)
    if node.right:
        get_leaves(node.right, d, lvl+1)

def make_structure(node, val=0):
    if not node:
         return
    return MyNode(val+1, make_structure(node.left, val+2), make_structure(node.right, val+3))

def find_paths(node):
    pass

    
if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8
    # print(count(Node(left=None, right=None))) # 0
    # print(count(Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))) # 2