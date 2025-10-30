class Node:
    data: str
    previous: "Node"
    next: "Node"


    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoubleLinkedList:
    head: Node
    tail: Node


    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        if self.head is not None and self.tail is not None:
            self.head.next = self.tail
            self.tail.previous = self.head

    
    def print_forward(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def print_backward(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.previous


    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is None:
            self.head.next = new_node
            new_node.previous = self.head
            self.tail = new_node
        elif self.head is None:
            self.head = self.tail
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node


    def prepend(self, new_data):
        new_node = Node(new_data)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is None:
            self.tail = self.head
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif self.head is None:
            self.tail.previous = new_node
            new_node.next = self.tail
            self.head = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.head is not None and self.tail is not None:
            current_node = self.head
            next_node = current_node.next

            if current_node.data == data:
                self.head = next_node
                if next_node is not None:
                    next_node.previous = None
                else:
                    self.tail = None
            else:
                while next_node is not None:
                    if next_node.data == data:
                        if next_node.next is None:
                            self.tail = current_node
                            current_node.next = None
                        else:
                            current_node.next = next_node.next
                            next_node.next.previous = current_node
                        break
                    current_node = next_node
                    next_node = current_node.next


my_double_list = DoubleLinkedList(Node("Init 1"), Node("Init 2"))
my_double_list.append("A")
my_double_list.append("B")
my_double_list.append("C")
my_double_list.prepend("X")
my_double_list.print_forward()
print("---")
my_double_list.delete("X")
my_double_list.print_forward()
print("---")
my_double_list.delete("Init 1")
my_double_list.print_forward()
print("---")
my_double_list.delete("Init 2")
my_double_list.print_forward()
print("---")
my_double_list.delete("A")
my_double_list.print_forward()
print("---")
my_double_list.delete("B")
my_double_list.print_forward()
print("---")
my_double_list.delete("C")
my_double_list.print_forward()
print("---")
my_double_list.delete("C")
my_double_list.print_backward()
