"""
16/03/2026 (UK)
Python Data Graphs
Jack Pearson
"""
class Graph():
    def __init__(self, vertices, edges):
        self.vertices = set(vertices)
        self.edges = set(edges)
        self.adjacencyList = {}
        self.adjacencyMatrix = {}
        self.matrix = [[[]] * len(vertices)] * len(vertices)
    
        # Adjacency List     
        for vertex in vertices:
            
            self.adjacencyList[vertex] = []

            for edge in edges:
                if vertex in edge:
                    for v in edge:
                        if v != vertex:
                            self.adjacencyList[vertex].append(v)
        
        # Adjacency matrix
        """
        self.adjacencyMatrix = {
            "a":{
                "a": 0,
                "b": 1,
                "c": 1
            },
            "b":{
                "a": 1,
                "b": 0,
                "c": 1
            },
            "c":{
                "a": 1,
                "b": 1,
                "c": 0
            }
        }    
        """

        for vertex in vertices:
            self.adjacencyMatrix[vertex] = {}

            for vert in vertices:
                self.adjacencyMatrix[vertex][vert] = 0

                for edge in edges:
                    if (vertex in edge) and (vert in edge) and (vertex != vert):
                        self.adjacencyMatrix[vertex][vert] = 1

    def printMatrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])



g = Graph(
    ["a", "b", "c"],
    [("a", "b"), ("b", "c"), ("a", "c"),]
)

print(g.adjacencyMatrix)
g.printMatrix()
#g.printMatrix()