from random import shuffle

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add_child(self, other):
        if self.left == None and self.value > other:
            self.left = Node(other)
        elif self.left:
            self.left.add_child(other)
        elif self.right == None and self.value < other:
            self.right = Node(other)
        else:
            self.right.add_child(other)

    def get_height(self, height=0):
        right = height
        left = height
        if self.right:
            right = self.right.get_height(height+1)
        if self.left:
            left = self.left.get_height(height +1)
        return max(right, left)
        
    
if __name__ == "__main__":
    a = [*range(10**5)]
    shuffle(a)
    root = Node(a[0])

    for i in range(1, len(a)):
        root.add_child(a[i])

    print(root.get_height())