class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class Queue():
    head: Node

    def __init__(self, head):
        self.head = head

    def print_all(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
    def enqueue(self, new_node):
        current_node = self.head
        next_node = current_node.next
        while (next_node is not None):
            current_node = next_node
            next_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node
    

third_node = Node("Third node")
second_node = Node("Second node", third_node)
first_node = Node("First node", second_node)

my_queue = Queue(first_node)
my_queue.print_all()
print()

print(f"Node deleted: {my_queue.dequeue().data}")
print()

my_queue.print_all()