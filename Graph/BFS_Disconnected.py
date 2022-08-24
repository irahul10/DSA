import queue
class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_matrix = [[0 for j in range(self.n_vertices)] for i in range(self.n_vertices)]
    
    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def bfs_diconnected(self):
        visited = [False for i in range(self.n_vertices)]
        for i in range(len(visited)):
            if visited[i] == False:
                q = queue.Queue()
                q.put(i)
                visited[i] = True
                while not q.empty():
                    current_node = q.get()
                    print(current_node)
                    for i in range(self.n_vertices):
                        if self.adj_matrix[current_node][i] == 1 and visited[i] == False:
                            q.put(i)
                            visited[i] = True

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)
g.bfs_diconnected()



