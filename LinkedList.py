class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Prepend a node at the start
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head needs to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the node to delete
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Node not found
        if temp is None:
            print(f"Node with data {key} not found.")
            return

        # Remove the node
        prev.next = temp.next
        temp = None

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example Usage:
llist = LinkedList()

# Build the list
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)
llist.append(4)

print("Original list:")
llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None

# Delete a node
llist.delete_node(2)
print("\nList after deleting node with data 2:")
llist.print_list()  # Output: 0 -> 1 -> 3 -> 4 -> None

# Delete head
llist.delete_node(0)
print("\nList after deleting head (0):")
llist.print_list()  # Output: 1 -> 3 -> 4 -> None
