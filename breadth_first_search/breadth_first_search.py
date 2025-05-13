from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, origin_vertex, destination_vertex):
        self.vertices[origin_vertex].append(destination_vertex)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            current_vertex = queue.popleft() # delete and get the first element
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.vertices[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)


graph_ = Graph()
graph_.add_vertex('A')
graph_.add_vertex('B')
graph_.add_vertex('C')
graph_.add_vertex('D')
graph_.add_edge('A', 'B')
graph_.add_edge('A', 'C')
graph_.add_edge('B', 'D')
graph_.bfs('A')

'''
    A
   / \
  B   C
  |
  D
'''