"""
23/02/2026 (UK)
Linked Lists
Jack Pearson
"""

class Node:
    def __init__ (self, data):
        self.data = data # the actual node value
        self.next = None # points at the.next node in the list

class LinkedList:
    def __init__ (self):
        self.head = None # holds the starting point
    
    def add(self, data):
        new_node = Node(data)
        if self.head is None: # when list is empty, head = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next: # goes to end of chain
                current = current.next
            current.next = new_node # appends new_node to end

    def get(self, index):
        current = self.head
        for items in range(index):
            if current == None:
                raise IndexError("Index out of range")
            current = current.next
        return current.data

    
lList = LinkedList()
lList.add(10)
lList.add(19)
lList.add(7)

print(lList.get(0))
print(lList.get(1))
    


        
