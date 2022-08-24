class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_matrix = [[0 for j in range(self.n_vertices)] for i in range(self.n_vertices)]

    
    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def dfs_helper(self, sv, ev, visited):
        if sv == ev:
            li = []
            li.append(sv)
            return li

        # print(sv)
        visited[sv] = True

        for i in range(self.n_vertices):
            if self.adj_matrix[sv][i] == 1 and visited[i] == False:
                ans = self.dfs_helper(i,ev,visited)
                if ans != None:
                    ans.append(sv)
                    return ans
        return None


    def dfs(self, sv, ev):
        visited = [False for i in range(self.n_vertices)]
        for i in range(self.n_vertices):
            if visited[i] == False:
                print(visited)
                print(self.dfs_helper(sv, ev, visited))



g = Graph(6)
g.add_edge(5, 3)
g.add_edge(0, 1)
g.add_edge(3, 4)
sv = int(input())
ev = int(input())
print(g.dfs(sv, ev))