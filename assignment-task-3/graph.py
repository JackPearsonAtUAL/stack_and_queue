class Graph:
	def __init__(self, vertices, edges):
		self.vertices = set(vertices)
		self.edges = edges

		# Adjacency list
		self.adjacency_list = {}
		for vertex in vertices:
			self.adjacency_list[vertex] = []

			for edge in edges.keys():
				if vertex in edge:
					for v in edge:
						if v != vertex:
							self.adjacency_list[vertex].append(v)
							break

		# Incidence matrix
		self.incidence_matrix = {}
		for vertex in vertices:
			self.incidence_matrix[vertex] = {}

			for edge in edges.keys():
				if vertex in edge:
					self.incidence_matrix[vertex][edge] = 1
				else:
					self.incidence_matrix[vertex][edge] = 0

		# Adjacency matrix
		self.adjacency_matrix = {}
		for vertex in vertices:
			self.adjacency_matrix[vertex] = {}

			for vertex2 in vertices:
				self.adjacency_matrix[vertex][vertex2] = 0

				for edge in edges.keys():
					if (vertex != vertex2) and (vertex in edge) and (vertex2 in edge):
						self.adjacency_matrix[vertex][vertex2] = 1

	def walk(self, source, target):
		# Attempt 1: Fail
		"""
		verts = list(self.vertices)
		matrix = self.adjacency_matrix

		start = verts.index(source) # Holds the starting node
		print(matrix[verts[start]])
		for a in matrix[verts[start]]:
			if (matrix[verts[start]][a] != 0):
				print(a)
		end = verts.index(target)  # holds the end node

		dist = [float('inf')] * len(verts) # Holds the distances between the source and current vertex
		dist[start] = 0 # dist[0] is referencing the starting vertex

		prev = [None] * len(verts) # Holds the data on all previous vertices

		visited = [False] * len(verts) # Boolean for whether the node has been visited yet

		for x in range(len(verts)):
			minDist = float('inf') # sets the smallest distance between start and next vertex
			u = None # u is the next vertex
			
			for i in range(len(verts)):
				# This comparison is used to determine the smallest distance
				if not visited[i] and dist[i] < minDist:
					minDist = dist[i] # Sets the new smallest distance
					u = i # Sets the current vertex
					print("Value of u:", u, "value of i:", i, "min distance =", minDist)
				
				# if there is no next node or we're at the target, end the loop
				if u is None or u == end:
					print("Breaking the loop. Current vertex:", verts[u]) # debug
					print("Distances:", dist) # debug
					break

				visited[u] = True # updates the code so it knows the current vertex has been visited
				print("Vertex visited:", verts[u]) # debug

				# Checks non visited adjacent vertices
				for v in range(len(verts)):
					# If the adjacent vertex has a shorter distance than the current, use this one instead
					if matrix[u][v] != 0 and not visited[v]:
						alt = dist[u] + matrix[u][v]
						if alt < dist[v]:
							dist[v] = alt
							prev[v] = u
		return prev + dist"""

		# Attempt 2: Fail
		"""
		verts = list(self.vertices)
		matrix = self.adjacency_matrix

		start = verts.index(source) # Holds the starting node
		end = verts.index(target)  # holds the end node

		dist = [float('inf')] * len(verts) # Holds the distances between the source and current vertex
		dist[start] = 0 # dist[0] is referencing the starting vertex

		visited = [False] * len(verts)
		visited[start] = True

		currentVert = start
		currentStep = None
		takenPath = [] # Holds the returned list

		possibleStep = []
		# Loop gets all the possible steps
		for x in matrix[verts[start]]:
			if (matrix[verts[start]][x] != 0):
				possibleStep.append(x)
				takenPath.append(currentVert)
				

		while(currentVert != end):
			# loop through each possible step to see which have a connection to the target
			for v in range(len(possibleStep)):
				# When there is no current step, set one
				if currentStep == None:
					currentStep = possibleStep[v]
				# Check current step can make it to the target
				for x in matrix[verts[v]]:					
					if matrix[verts[v]].get("d") != 1:									
						print("ln 121, no target found; current step =", currentStep)
						print(matrix[verts[v]].get("d"))
						currentStep = None
						
						break
					else:	
						print("Target has been found; possible step =", possibleStep[v])					
						# if it can make sure there isn't already a step
						if currentStep != possibleStep[v] and currentStep != None:
							print("debug 3")
							# if there is a step, compare the distances
							if matrix.get(currentStep) < matrix.get(possibleStep[v]):
								# the shorter distance is the new step
								currentStep = possibleStep[v]
								print("Current step:",currentStep)
								print("Possible step:",possibleStep[v])
					break
				print("Current step is:", currentStep)				

					

			break
		return takenPath"""

		# Attempt 3: Success
		"""
		1. Create set() of unvisited nodes
		2. Create variable for distances. Each distance is float('inf') until found
		3. From unvisited set, find node with smallest distance to set new current node
			if unvisited set is empty or contains nodes with float('inf'), algorithm skips to setp 6.
		4. For current node, look at all unvisited neibours
			compare newly calculated distance to the current distance of the neighbour:
				current node distance + edge value = new neighbour distance
			 update distance to be the smallest distance
		5. Look at all unvisited neighbour nodes, current node is removed from unvisited set. This stops it from being rechecked
		6. Once loop ends (3. -> 5.) every visited node has it's shortest node
		"""

		unvisited = self.vertices
		distance = dict() # Holds the distances between each of the nodes
		previous = dict() # Holds all the previously vistied nodes and which node they came from
			
		for v in unvisited:
			distance[v] = float('inf')
			previous[v] = None

		distance[source] = 0
		currentNode = source

		while(len(unvisited) > 0):
			smallestDist = float('inf')

			# Get current node
			for n in distance:
				if distance[n] < smallestDist and n in unvisited:
					currentNode = n
					smallestDist = distance[n]

			if currentNode != target and smallestDist != float('inf'):
				# Get all neighbour nodes
				for n in self.adjacency_list[currentNode]:
					# Check that n hasn't been visited
					if n in unvisited:
						# Calculate the total distance between cNode and neighbour
						tempDist = distance[currentNode] + self.edges[(currentNode, n)]

						# If value is smaller than the current distanc, it is the new distance
						if tempDist < distance[n]:
							distance[n] = tempDist
							previous[n] = currentNode

				unvisited.remove(currentNode)	
			# Ends the while if the target has been reached
			else:
				break
		

		"""
		Pseudocode from the wikapedia article on Dijkstra's algorithm
		1  S ← empty sequence
		2  u ← target
		3  if prev[u] is defined or u = source:    // Proceed if the vertex is reachable
		4      while u is defined:                 // Construct shortest path with stack S
		5          S.push(u)                       // Push the vertex onto the stack
		6          u ← prev[u]                     // Traverse from target to source
		"""
		path = []
		iteration = target
		if previous[iteration] != None or iteration == source:
			while iteration != None:
				path.insert(0, iteration)
				iteration = previous[iteration]
			
		return path

