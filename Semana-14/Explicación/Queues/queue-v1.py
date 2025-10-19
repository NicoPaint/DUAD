class Node:
  data: str

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


""" En esta versión, Queue hereda de LinkedList en vez de escribir todo el código en ella  """
class Queue(LinkedList):
  
  def enqueue(self, new_node):
    current_node = self.head
    next_node = current_node.next
    while (next_node is not None):
      current_node = next_node
      next_node = current_node.next

    current_node.next = new_node

  def dequeue(self):
    self.head = self.head.next