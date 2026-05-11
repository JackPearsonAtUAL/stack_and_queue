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
		verts = list(self.vertices)
		start = verts.index(source) # Holds the starting node
		end = verts.index(target)  # holds the end node

		dist = [float('inf')] * len(verts) # Holds the distances between the source and current vertex
		prev = [None] * len(verts) # Holds the data on all previous vertices

		dist[0] = 0 # dist[0] is referencing the starting vertex

		visited = [False] * len(verts) # Boolean for whether the node has been visited yet

		for x in range(len(verts)):
			minDist = float('inf') # sets the smallest distance between start and next vertex
			u = None # u is the next vertex
			
			for i in range(len(verts)):
				# This comparison is used to determine the smallest distance
				if not visited[i] and dist[i] < minDist:
					minDist = dist[i] # Sets the new smallest distance
					u = i # Sets the next vertex
					print("Value of u:", u, "value of i:", i, "min distance =", minDist)
				
				# if there is no next node or we're at the target, end the loop
				if u is None or u == end:
					print("Breaking the loop. Current vertex:", verts[u]) # debug
					print("Distances:", dist) # debug
					break

				visited[u] = True # updates the code so it knows the current vertex has been visited
				print("Vertex visited:", verts[u]) # debug

				for v in range(len(verts)):
					# makes sure that the current iteration is valid and that v hasn't been visited
					if self.adjacency_matrix[u][v] != 0 and not visited[v]:
						alt = dist[u] + self.adjacency_matrix[u][v]			
						if alt < dist[v]:
							dist[v] = alt

		return dist

