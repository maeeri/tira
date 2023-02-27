from collections import namedtuple

def diff(node):
    return get_max(node)

def get_knots(node, knots=0):
    knots_left = 0 if node.left == None else get_knots(node.left, knots+1)
    knots_right = 0 if node.right == None else get_knots(node.right, knots+1)
    knots = knots_left + knots_right + 1
    return knots

def get_max(node, max_diff=0):
    left = 0
    right = 0
    left_max = 0
    right_max = 0
    if node.left != None:
        left = get_knots(node.left)
        left_max = get_max(node.left, max_diff)
    if node.right != None:
        right = get_knots(node.right)
        right_max = get_max(node.right, max_diff)
    return max(max_diff, left_max, right_max, abs(left-right))

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    print(diff(tree)) # 4
    tree = Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=None))), right=Node(left=Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))), right=None), right=None))
    print(diff(tree)) # 5
    tree = Node(left=None, right=Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))
    print(diff(tree)) # 3
