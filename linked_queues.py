"""
23/02/2026 (UK)
Queues Using Liked Lists
Jack Pearson
"""

class Node:
    def __init__ (self, data):
        self.data = data # the actual node value
        self.next = None # points at the next node in the list

class Queue:
    def __init__ (self):
        self.front = None
        self.back = None
        self.currentSize = 0
        self.maxLength = 10
    
    # adds new entry to queue
    def enqueue(self, data):
        if self.currentSize < self.maxLength:
            newNode = Node(data)
            if self.isEmpty(): # when there are no data entries
                self.front = self.back = newNode # make the current piece of data the front, back and new
            else:
                self.back.next = newNode
                self.back = newNode
            self.currentSize += 1
        else:
            self.isFull()
    
    # removes item from queue
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")

        removed = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None     

        self.currentSize -= 1
        return removed
    
    # gets element at the front of the queue
    def getFront(self):
        if self.isEmpty():
            raise IndexError("Queue Underflow")
        return self.front.data

    # checks if queue is empty
    def isEmpty(self):
        return self.front is None
    
    # used to check the size of the queue
    def size(self):
        return self.currentSize
    
    def isFull(self):
        print("Queue Upper Index Limit Reached")
q = Queue()

q.enqueue(10)
q.enqueue(20)
print(f"Front: {q.getFront()}")
print("")

print("Dequeue:", q.dequeue())

q.enqueue(30)

print(f"Front: {q.getFront()}")
print(f"Size: {q.size}")

q.dequeue()
q.dequeue()

for i in range(11):
    q.enqueue(i)
