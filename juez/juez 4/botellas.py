def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin,dest):
    n = len(g) - 1
    distances = [float('inf')] * n
    visited = [False] * n
    rever=[-5]*n
    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
        rever[end]=start
    for _ in range(0, len(g)): #Bucle voraz
        for start, end, weight in g[_]:
            if end !=origin and rever[end]==-1:
                rever[end] = start
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if distances[end]>distances[start]+weight:
                rever[end] = start
            distances[end] = min(distances[end], distances[start] + weight)
    node=dest
    path=[]
    while node !=origin:
        path.append(node)
        node=prev[node]
    path.append(origin)
    return distances[dest],path

def  botella (grafo,s,e):
    sol,path=dijkstra(grafo,s,e)
    print(sol)
    path.reverse()
    print(path)

n, m = map(int, input().strip().split())
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    origen, destino, peso = map(int, input().strip().split())
    grafo[origen].append((origen, destino, peso))
    grafo[destino].append((destino, origen, peso))
s,e= map(int, input().strip().split())
botella(grafo,s,e)
