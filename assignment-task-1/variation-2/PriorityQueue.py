"""
Variation 2: 
Insertion Sort the queue using the priority value stored within a queued value
"""

class PriorityQueue:
	def __init__(self, data):
		self.queue = []

		# Loops through each object in data, adding it to the self.queue as a list
		for i in range(len(data)):
			self.queue.append(list(data[i]))

		self.insertSort()

	def get(self):
		popped = self.queue[0][0] # Gets string value of first object in queue
		self.queue.pop(0) # Removes first item of queue
		return popped

	def add(self, data):
		self.queue.append(data)
		# Performs a Insertion Sort on the self.queue
		self.insertSort()
	
	def insertSort(self):
		# Loop through each object in self.queue
		for i in range(len(self.queue)):
			currentVal = self.queue.pop(i) # Holds the current object being checked
			insertIndex = i
			# Loop through all other objects in list (backwards), comparing them to the in currentVal	
			for j in range(i-1, -1, -1):
				if self.queue[j][1] > currentVal[1]:
					insertIndex = j
			
			self.queue.insert(insertIndex, currentVal)

				
