from collections import namedtuple

def count(node, counter=0):
    if not node or not node.left and not node.right:
        return 1
    if node.left or node.right:
        return count(node.left, counter+1) + count(node.right, counter+1)


if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 2
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8


# Tehtäväsi on laskea, montako lehteä on annetussa binääripuussa. 
# Voit olettaa, että puussa on enintään 100 solmua.

# Tehtäväpohjassa on esimerkkinä seuraava puu, jossa on kaksi lehteä:
# o
#  \
#   o
#  / \
# o   o

# Toteuta tiedostoon leaves.py funktio count, joka palauttaa lehtien määrän.