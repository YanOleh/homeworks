from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_scc(self, u, low, disc, stack_member, st):
        static_counter = 0

        disc[u] = low[u] = static_counter
        static_counter += 1
        stack_member[u] = True
        st.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.dfs_scc(v, low, disc, stack_member, st)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                stack_member[w] = False
            print("")

    def strongly_connected_components(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        st = []

        for i in range(self.V):
            if disc[i] == -1:
                self.dfs_scc(i, low, disc, stack_member, st)


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
g.strongly_connected_components()
