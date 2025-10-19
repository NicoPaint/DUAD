class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next