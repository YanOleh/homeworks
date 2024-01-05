from collections import deque


def bfs_shortest_path(graph, start):
    queue = deque([(start, 0)])
    visited = set([start])
    distances = {start: 0}

    while queue:
        current_vertex, current_distance = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance = current_distance + 1
                distances[neighbor] = distance
                queue.append((neighbor, distance))

    return distances


def all_pairs_shortest_path(graph):
    all_shortest_paths = {}

    for vertex in graph:
        shortest_paths = bfs_shortest_path(graph, vertex)
        all_shortest_paths[vertex] = shortest_paths

    return all_shortest_paths


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

result = all_pairs_shortest_path(graph)

for vertex in result:
    print(f"Shortest paths from {vertex}: {result[vertex]}")
