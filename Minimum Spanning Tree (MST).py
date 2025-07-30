import heapq
graph_data = {
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 3),
        ('B', 'D', 4),
        ('C', 'D', 2)
    ],
    'adj_list': {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 3), ('D', 4)],
        'C': [('A', 3), ('B', 3), ('D', 2)],
        'D': [('B', 4), ('C', 2)]
    }
}
def prim(graph, start):
    visited = set()
    mst = []
    min_heap = [(0, start, None)]  # (ağırlık, düğüm, parent)

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if parent:
                mst.append((parent, node, weight))
            for neighbor, w in graph['adj_list'][node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, node))
    return mst
print("\nPrim MST (başlangıç: A):")
for edge in prim(graph_data, 'A'):
    print(edge)




# Kruskal için Union-Find (Disjoint Set)
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

# Kruskal algoritması
def kruskal(graph):
    mst = []
    edges = sorted(graph['edges'], key=lambda x: x[2])  # ağırlığa göre sırala
    ds = DisjointSet(graph['vertices'])

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

print("Kruskal MST:")
for edge in kruskal(graph_data):
    print(edge)