# Attack function
def attack(graph):
    res = kruskal(graph)
    print(res)
    if res % 5 > 0:
        res = int(res / 5) + 1
    else:
        res = int(res // 5)
    print(res)


def kruskal(g):
    candidates = sortdata(g)
    components = list(range(len(g)))
    count = len(components)
    sol = 0
    i = 0
    while count >  0 and i < len(candidates):
      (weight, start, end) = candidates[i]
      if components[start] != components[end]:
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
      i += 1
      return sol


# Update the components
def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def sortdata(graph):
    candidates = []
    n = len(graph)
    for i in range(n):
     for adj in graph[i]:
         candidates.append([adj[1], i, adj[0]])

    candidates.sort()
    return candidates

# Main programme
n, m = map(int, input().strip().split())
graph = []
for i in range(n):
    graph.append([])
for i in range(m):
    n1, n2, d = map(int, input().strip().split())
    graph[n1].append([n2, d])
attack(graph)
