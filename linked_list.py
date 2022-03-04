# linked list in data structure

class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    # Print the linked list
    def list_print(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next_val

    def insert_at_begining(self, new_data):
        new_node = Node(new_data)

        # Update the new nodes next val to existing node
        new_node.next_val = self.head_val
        self.head_val = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if not self.head_val:
            self.head_val = new_node
            return
        last_node = self.head_val
        while last_node.next_val:
            last_node = last_node.next_val
        print("new node added at the end")
        last_node.next_val = new_node


linked_list = LinkedList()
linked_list.head_val = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")

linked_list.head_val.next_val = node2
node2.next_val = node3

linked_list.insert_at_begining("Sun")
print("linked list after adding new node at beginning.......")
linked_list.list_print()
print("linked list after adding new node at end.......")
linked_list.insert_at_end("thu")
linked_list.list_print()
