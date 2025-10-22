class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    head: Node

    def __init__(self, head):
        self.head = head
    

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        if self.head:
            self.head = self.head.next


first_node = Node("First node")
second_node = Node("Second node", first_node)
third_node = Node("Third node", second_node)

my_stack = Stack(third_node)
my_stack.print_structure()
print()

my_stack.pop()
my_stack.print_structure()
print()

my_stack.push(Node("New third node"))
my_stack.print_structure()
print()

my_stack.push(Node("Fourth node"))
my_stack.print_structure()