"""
Variation 1: 
Bubble sort queue using the priority value stored within a queued value
"""
class PriorityQueue:
    def __init__(self, data):
        self.queue = []

        # Loops through each object in data, adding it to the self.queue as a list
        for i in range(len(data)):
            self.queue.append(list(data[i]))

        # Performs a bubble sort on the self.queue
        self.bubbleSort()


    def get(self):
        popped = self.queue[0][0] # Gets string value of first object in queue
        self.queue.pop(0) # Removes first item of queue
        return popped

    def add(self, data):
        self.queue.append(data)
        # Performs a bubble sort on the self.queue
        self.bubbleSort()

    def bubbleSort(self):
        """
        Base for the bubble sort from:
        https://www.w3schools.com/python/python_dsa_bubblesort.asp
        """
        # Loops through the queue one object at a time
        for i in range(len(self.queue) - 1):
            # swapped is used to check whether or not self.queue is already sorted
            swapped = False
            # Internal loop to compare every object in the queue to self.queue[i]
            for j in range(len(self.queue) - i - 1):
                # When the current queue obejct has a greater priority value than the next, swap them
                if self.queue[j][1] > self.queue[j+1][1]:
                    self.queue[j], self.queue[j+1] = self.queue[j+1], self.queue[j]
                    swapped = True
            # Ends loop if it is already sorted
            if not swapped:
                break
