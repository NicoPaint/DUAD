class Node:
    data: int
    next: "Node"

    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


class Linkedlist:
    head: Node

    def __init__(self, head = None):
        self.head = head
    

    @property
    def length(self):
        current_node = self.head
        total = 0
        while current_node is not None:
            total += 1
            current_node = current_node.next
        
        return total


    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    
    def insert_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    

    def insert_back(self, new_data):
        new_node = Node(new_data)

        if self.head is not None:
            current_node = self.head
            next_node = current_node.next
            while next_node is not None:
                current_node = next_node
                next_node = current_node.next

            current_node.next = new_node
        else:
            self.head = new_node


    def delete(self, data):
        if self.head is not None:
            current_node = self.head
            next_node = current_node.next

            if current_node.data == data:
                self.head = next_node
            else:
                while next_node is not None:
                    if next_node.data == data:
                        current_node.next = next_node.next
                        break
                    current_node = next_node
                    next_node = current_node.next