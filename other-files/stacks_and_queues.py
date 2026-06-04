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
            return "Stack is empty."
        else:
            return self.stack.pop()
    
    # Prints out the first (front) element in the stack
    def peek(self):
        if self.isEmpty:
            return "Stack is empty."
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
            return "Queue is empty."
        else:
            return self.queue.pop(0)
    
    # Prints out the first (front) element in the stack
    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        else:
            return self.queue[0]

    # Bool check if the queue is empty or not    
    def isEmpty(self):
        return len(self.queue) == 0
    
    # returns the size of the queue
    def size(self):
        return len(self.queue)

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

print("")

myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Enqueue: ", myQueue.dequeue())
print("Queue after Pop: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
