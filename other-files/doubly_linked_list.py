"""
23/02/2026 (UK)
Doubly Linked Lists
Jack Pearson
"""

class DoublyNode:
    def __init__ (self, data):
        self.data = data # the actual node value
        self.next = None # points at the next node in the list
        self.prev = None # points at the previous node in the list

class DoublyLinkedList:
    def __init__ (self):
        self.head = None # holds list front
        self.tail = None # holds list back
    
    def add(self, data):
        new_node = DoublyNode(data)
        if self.head is None: # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail # new_node looks back at the old tail
            self.tail.next = new_node # old tail looks at new_node
            self.tail = new_node # new_node is now tail
    
    def addFront(self, data):
        new_node = DoublyNode(data)
        if self.head is None: # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = new_node           
            self.head = new_node

    def get(self, index):
        current = self.head
        for items in range(index):
            if current == None:
                raise IndexError("Index out of range")
            current = current.next
        return current.data, self.get_front(), self.get_back()

    def get_front(self):
        if self.head is None:
            raise IndexError("List is empty")
        return self.head.data
    
    def get_back(self):
        if self.tail is None:
            raise IndexError("List is empty")
        return self.tail.data 
    
dll = DoublyLinkedList()

dll.add(10)
dll.add(20)
dll.add(30)
dll.add(40)

print(f"Front is: {dll.get(2)[1]}, Tail is: {dll.get(2)[2]}")

dll.addFront(50)

print(f"Front is: {dll.get(2)[1]}, Tail is: {dll.get(2)[2]}")
print(dll.get(0)[0])
print(dll.get(1)[0])
print(dll.get(2)[0])
print(dll.get(3)[0])
print(dll.get(4)[0])
