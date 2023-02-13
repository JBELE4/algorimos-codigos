# Botellines function
from collections import deque


def botellines(candidates, s, e):
# We use Dijkstra here. From s, get the minimum distance to e
    sol, path = dijkstra(candidates, s, e)
    print(sol)
    path.reverse()
    print(str(path).replace("[","").replace("]","").replace(",",""))

def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem


def dijkstra(g, origin, dest):
    n = len(g)
    distances = [float('inf')] * n
    visited = [False] * n
    prev = [-1] * n
    distances[origin] = 0
    visited[origin] = True #Start visiting the graph
    for start, end, weight in g[origin]:
        distances[end] = weight
        prev[end] = start

    for i in range(0, len(g)):  # Greedy loop
        for start, end, weight in g[i]:
            if end != origin and prev[end] == -1:
                prev[end] = start

        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if distances[end] > distances[start] + weight:
                prev[end] = start
                print(prev[end],"dos")
            distances[end] = min(distances[end], distances[start] + weight)

    node = dest
    path = []
        # visit the nodes back and retrieve the path
    print(node)
    while node != origin:
        print(node,"1")
        path.append(node)
        print(node,"2")
        node = prev[node]
        print(node,"3")
    path.append(origin)
    return distances[dest], path
# MAIN PROGRAMME
bottles = []

n, m = map(int, input().strip().split())
for _ in range(n):
    bottles.append([])

for _ in range(m):
    c1, c2, d = map(int, input().strip().split())
    bottles[c1].append([c1, c2, d])
    bottles[c2].append([c2, c1, d])
s, e = map(int, input().strip().split())
botellines(bottles, s, e)
