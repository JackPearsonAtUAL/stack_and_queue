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
		# Attempt 1
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

		# Attempt 2
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
		return []

