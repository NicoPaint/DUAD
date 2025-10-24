class Node:
    data: str
    child_left: "Node"
    child_right: "Node"

    def __init__(self, data, child_left=None, child_right=None):
        self.data = data
        self.child_left = child_left
        self.child_right = child_right


class BinaryTree:
    root: Node

    def __init__(self, root):
        self.root = root

    
    def print_structure(self):
        self.map_the_tree(self.root)
    
    """ This algorithm will map de tree from root to the deepest level """
    def map_the_tree(self, none):
        if none == None:
            return
        print(none.data)
        self.map_the_tree(none.child_left)
        self.map_the_tree(none.child_right)


left_child_of_left_child = Node("Soy left child of left child")
right_child_of_left_child = Node("Soy right child of left child")
left_child_of_right_child = Node("Soy left child of right child")
right_child_of_right_child = Node("Soy right child of right child")
left_child = Node("Soy left child of root", left_child_of_left_child, right_child_of_left_child)
right_child = Node("Soy right child of root", left_child_of_right_child, right_child_of_right_child)
root_node = Node("Soy root", left_child, right_child)

my_binary_tree = BinaryTree(root_node)

my_binary_tree.print_structure()