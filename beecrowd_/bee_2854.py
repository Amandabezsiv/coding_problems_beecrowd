M, N = list(map(int, input().split()))
G = []

for i in range(N):
    G.append(input().split())
graph = {}

for i in G:
    vertex, edge, neighbor = i
    if vertex not in graph:
        graph[vertex] = []
    if neighbor not in graph:
        graph[neighbor] = []
    graph[vertex].append(neighbor)
    graph[neighbor].append(vertex)

nodes = list(graph.keys())
n_family = 0

while nodes:

    queue = [(nodes[0], {i: False for i in nodes})]
    queue[0][1][nodes[0]] = True

    while queue:

        current_node, visited = queue.pop(0)

        for neighbor in graph[current_node]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append((neighbor, visited))
            try:
                nodes.remove(neighbor)
            except:
                pass
    n_family += 1

print(n_family)
