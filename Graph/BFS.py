import queue
class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_matrix = [[0 for i in range(self.n_vertices)] for i in range(self.n_vertices)]

    
    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    
    def bfs(self):
        visited = [False for i in range(self.n_vertices)]
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while not q.empty():
            current_node = q.get()
            print(current_node)
            for i in range(self.n_vertices):
                if self.adj_matrix[current_node][i] == 1 and visited[i] == False:
                    q.put(i)
                    visited[i] = True
        

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.bfs()
                    