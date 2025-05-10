class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edges(self, origin_vertex, destination_vertex):
        self.vertices[origin_vertex].append(destination_vertex)

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)
    
    def _dfs(self, vertex, visited):
        print(vertex)
        visited.add(vertex)
        for next in self.vertices[vertex]:
            if next not in visited:
                self._dfs(next, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                # Agregamos los vecinos al stack (en orden inverso si queremos simular el mismo recorrido)
                for neighbor in reversed(self.vertices[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)


'''
Graph

   A
  / \
 B   C
 |
 D

'''

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edges('A', 'B')
graph.add_edges('A', 'C')
graph.add_edges('B', 'D')
graph.dfs('A')
print("***")
graph.dfs_iterative('A')