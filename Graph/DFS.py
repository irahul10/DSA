class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_matrix = [[0 for j in range(self.n_vertices)] for i in range(self.n_vertices)]


    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0
    
    def dfs_helper(self, sv, visited):
        print(sv)
        visited[sv] = True

        for i in range(self.n_vertices):
            if self.adj_matrix[sv][i] > 0 and visited[i] == False:
                self.dfs_helper(i, visited)
            

    def dfs(self):
        visited = [False for i in range(self.n_vertices)]
        self.dfs_helper(0, visited) 

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.dfs()