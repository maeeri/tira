from collections import namedtuple

def count(node, level):
    knots = get_knots(node, level)
    return knots

def get_knots(node, level, l=1):
    knots = 0
    if l==level:
        return 1
    if l < level:
        if node.left != None:
            knots += get_knots(node.left, level, l+1)
        if node.right != None:
            knots += get_knots(node.right, level, l+1)
    return knots


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0