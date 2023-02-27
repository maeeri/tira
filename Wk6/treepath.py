from collections import namedtuple

def count(node):
    paths = all_paths(node)
    result = 0
    for path in paths:
        if len(path) > 1:
            counter = 0
            for node in path:
                print(node)
                counter += 1
            result += counter - 1
    return result

def all_paths(node):
    if not node:
        return []
    if node.left is None and node.right is None:
        return [[node]]
    left_paths = all_paths(node.left)
    right_paths = all_paths(node.right)
    return [[node] + path for path in left_paths + right_paths]
    
if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8
    print(count(Node(left=None, right=None))) # 0
    print(count(Node(left=Node(left=None, right=None), right=Node(left=None, right=None)))) # 2