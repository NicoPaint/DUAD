class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleEndedQueue:
    head: Node

    def __init__(self, head):
        self.head = head

    
    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node
    
    
    def push_right(self, new_node):
        current_node = self.head
        next_node = current_node.next
        while next_node is not None:
            current_node = next_node
            next_node = current_node.next
        
        current_node.next = new_node


    def pop_left(self):
        if self.head:
            self.head = self.head.next
    

    def pop_right(self):
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                current_node = self.head
                next_node = current_node.next
                while next_node.next is not None:
                    current_node = next_node
                    next_node = current_node.next
                
                current_node.next = None


third_node = Node("Third node")
second_node = Node("Second node", third_node)
first_node = Node("First node", second_node)

my_double_queue = DoubleEndedQueue(first_node)
print("Initial structure")
my_double_queue.print_structure()
print()

my_double_queue.push_left(Node("Zero node"))
print("Adding at the beginning of the queue")
my_double_queue.print_structure()
print()

my_double_queue.push_right(Node("Fourth node"))
print("Adding at the end of the queue")
my_double_queue.print_structure()
print()

my_double_queue.pop_left()
print("Deleting at the beginning of the queue")
my_double_queue.print_structure()
print()

my_double_queue.pop_right()
print("Deleting at the end of the queue")
my_double_queue.print_structure()
print()