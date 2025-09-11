# A simple linked list implementation in Python

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head=None
    
    # add a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # add a new node at the start of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

llist=Linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)

llist.head.next=second
second.next=third

llist.printlist()

# This code defines a simple linked list with three nodes and prints their values.
# A linked list is a linear data structure where each element is a separate object, with each element (node) containing a reference (link) to the next node in the sequence.
# This allows for efficient insertions and deletions, as nodes can be easily added or removed without reorganizing the entire structure.
# Linked lists are dynamic in size, meaning they can grow and shrink as needed, unlike arrays which have a fixed size.
# Linked lists can be singly linked (where each node points to the next node) or doubly linked (where each node points to both the next and previous nodes).
# Linked lists are commonly used in scenarios where frequent insertions and deletions are required, such as in implementing stacks, queues, and other dynamic data structures.
# Linked lists are also used in various algorithms and applications, including memory management, graph representations, and more.
# Linked lists can be traversed by following the links from one node to the next, starting from the head of the list.
# Linked lists can be implemented in various programming languages, including Python, C, C++, and Java.
# Linked lists can be used to implement adjacency lists in graph representations, where each vertex points to a linked list of its adjacent vertices.
# Linked lists can be used to implement polynomial representations, where each term in the polynomial is represented
# as a node in the linked list.
# Linked lists can be used to implement navigation systems, where each location is represented as a node in the linked list.
# Linked lists can be used to implement undo/redo functionality in applications, where each action is represented as a node in the linked list.