N, M = list(map(int, input().split()))
graph = [[] for i in range(N)]
cities = [i for i in range(N)]
for i in range(M):
    U, V, W = map(int, input().split())
    graph[U].append((V, W))
    graph[V].append((U, W))


def dijkstra(g, origin):
    distance = [float("inf")] * N
    distance[origin] = 0
    queue = [(0, origin)]

    while queue:
        current_weigth, current_node = queue.pop(0)

        for neighbor, edge in graph[current_node]:
            new_weight = edge + distance[current_node]
            if new_weight < distance[neighbor]:
                distance[neighbor] = new_weight
                queue.append((edge, neighbor))
                queue.sort()
    return distance


maximus = []
for i in cities:
    maximus.append(max(dijkstra(graph, i)))

print(min(maximus))
