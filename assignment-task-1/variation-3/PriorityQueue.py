"""
Variation 3: 
Counting Sort the queue using the priority value stored within a queued value
"""

class PriorityQueue:
	def __init__(self, data):
		self.queue = []	
		self.minPrio = 0
		self.maxPrio = 5

		# Loops through each object in data, adding it to the self.queue as a list
		for i in range(len(data)):
			self.queue.append(list(data[i]))


		self.counts = [[], [], [], [], [], []] #[holds all queue prios[pos based on queue prio[holds queue data]]]
		self.countSort()

	def get(self):
		popped = self.queue[0][0] # Gets string value of first object in queue
		self.queue.pop(0) # Removes first item of queue
		return popped
		

	def add(self, data):
		self.queue.append(list(data))
		# Performs a Counting Sort sort on the self.queue
		self.countSort()

	def countSort(self):
		# Loops until the list of inputted data is empty
		while len(self.queue) != 0:
			temp = self.queue.pop(0) # Holds the data at the current index
			
			# Becuase the priority queue values start at 1, 
			# I lowered them by one so that the counts list 
			# didn't have an empty nested list
			index = temp[1]-1 

			# Adds the temp value to the nested list based on it's value
			self.counts[index].append(temp)
		# Loops through the now filled counts' nested lists
		for i in range(0, 6):
			# Loops through the current nested list untilis is empty
			while len(self.counts[i]) != 0:
				# Holds the data at the current index, 
				# while also removing it from the list
				temp = self.counts[i].pop(0)

				#Adds the data back to the original list to be returned to main.py
				self.queue.append(temp)
					
					
		
		