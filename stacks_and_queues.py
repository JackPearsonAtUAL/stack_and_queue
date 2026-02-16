"""
16/02/2026 (UK)
Stacks and Queues
Jack Pearson
"""

class Stack:
    # Initialises itself
    def __init__(self):
        self.stack = []

    # Adds data to the stack
    def push(self, data):
        self.stack.append(data)

    # Removes and returns the first (front) element in the stack
    def pop(self):
        if self.isEmpty:
            print("Stack is empty.")
        else:
            return self.stack.pop()
    
    # Prints out the first (front) element in the stack
    def peek(self):
        if self.isEmpty:
            print("Stack is empty.")
        else:
            return self.stack[-1]
        
    def isEmpty(self):
        return len(self.stack) == 0
       
    def size(self):
        return len(self.stack)

class Queue:
    # Initialises self
    def __init__(self):
        self.queue = []

    # Adds value to the end of the queue
    def enqueue(self, data):
        self.queue.append(data)

    # Removes and returns the first (front) element from the queue
    def dequeue(self):
        if self.isEmpty:
            print("Stack is empty.")
        else:
            return self.stack.pop()
    
    # Prints out the first (front) element in the stack
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.stack.pop()

    # Bool check if the queue is empty or not    
    def isEmpty(self):
        return len(self.stack) == 0
    
    # returns the size of the queue
    def size(self):
        return len(self.stack)

myStack = Stack()
myQueue = Queue()
