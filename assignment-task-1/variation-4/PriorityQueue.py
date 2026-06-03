"""
Variation 4: 
Merge Sort the queue using the priority value stored within a queued value
"""
class PriorityQueue:
	def __init__(self, data):
		self.queue = []	
		
		# Loops through each object in data, adding it to the self.queue as a list
		for i in range(len(data)):
			self.queue.append(list(data[i]))

		self.queue = self.mergeSort(self.queue)

	def get(self):
		popped = self.queue[0][0] # Gets string value of first object in queue
		self.queue.pop(0) # Removes first item of queue
		return popped
		

	def add(self, data):
		queueSize = len(self.queue)
		currentValue = 0
		while queueSize == len(self.queue):
			if self.queue [currentValue][1] > data[1]:
				self.queue.insert(currentValue, data) 
			else:
				currentValue +=1

		# Removed the sort after adding, as it will mess up the order in which items are returned.
		#self.mergeSort(self.queue)


	def merge(self, left, right):
		result = []
		i = j = 0

		while i < len(left) and j < len(right):
			if left[i][1] < right[j][1]:
				result.append(left[i])
				i += 1
			elif left[i][1] == right[j][1]:
				if ord(left[i][0][0]) < ord(right[j][0][0]):
					result.append(left[i])
					i += 1
				elif ord(left[i][0][0]) == ord(right[j][0][0]):
					if ord(left[i][0][1]) < ord(right[j][0][1]):
						result.append(left[i])
						i += 1
					else:
						result.append(right[j])
						j += 1
				else:
					result.append(right[j])
					j += 1
			else:
				result.append(right[j])
				j += 1

		result.extend(left[i:])
		result.extend(right[j:])

		return result

	
	def mergeSort(self, _queue):
		step = 1 # Starting with sub-arrays of length 1
		length = len(_queue)

		while step < length:
			for i in range(0, length, 2 * step):
				left = _queue[i:i + step]
				right = _queue[i + step:i + 2 * step]

				merged = self.merge(left, right)

				# Place the merged array back into the original array
				for j, val in enumerate(merged):
					_queue[i + j] = val

			step *= 2 # Double the sub-array length for the next iteration

		#_queue = self.alphabetSort(_queue)

		return _queue
	

				
