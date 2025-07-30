import heapq
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 5},
    'D': {}
}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dist, node = heapq.heappop(queue)
        for neighbor, weight in graph[node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

print(dijkstra(graph, 'A'))
print("\n")




def bellman_ford(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    for _ in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                weight = graph[u][v]
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Negatif döngü kontrolü
    for u in graph:
        for v in graph[u]:
            if distance[u] + graph[u][v] < distance[v]:
                raise Exception("Negatif ağırlıklı döngü var!")

    return distance

print(bellman_ford(graph, 'A'))
print("\n")




def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    
    for u in nodes:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

from pprint import pprint
pprint(floyd_warshall(graph))

