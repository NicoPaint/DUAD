from LinkedList import Linkedlist

def sort_linked_list(linked_list):
    for outer_index in range(0, linked_list.length - 1):

        did_they_change = False

        current_node = linked_list.head
        next_node = current_node.next
        if current_node.data > next_node.data:
            linked_list.head.next = next_node.next
            next_node.next = linked_list.head
            linked_list.head = next_node
            next_node = current_node.next
        else:
            current_node = linked_list.head.next
            next_node = current_node.next
        
        counter = 1
        while counter < (linked_list.length - 1 - outer_index):
            
            if current_node.data > next_node.data:

                current_node.next = next_node.next
                next_node.next = current_node

                previus_node = linked_list.head
                while previus_node.next != current_node:
                    previus_node = previus_node.next
                
                previus_node.next = next_node
                next_node = current_node.next

                did_they_change = True
            else:
                current_node = next_node
                next_node = current_node.next

            counter += 1

        if not did_they_change:
            break

""" Function Test """
my_linked_list = Linkedlist()
my_linked_list.insert_back(37)
my_linked_list.insert_back(3)
my_linked_list.insert_back(33)
my_linked_list.insert_back(30)

my_linked_list.print_all()
sort_linked_list(my_linked_list)
print()
my_linked_list.print_all()