def viaje(grafo):
 sol=[]*len(grafo)
 resultado=0
 for i in range(len(grafo)):
     sol.append(dijkstra(grafo,i))
     for a in  sol[i]:
         if resultado<a:
             resultado=a



 print(resultado)


def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(0, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] *n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
    for _ in range(len(g)): #Bucle voraz
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances

n, m = map(int, input().strip().split())
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    origen, destino, peso = map(int, input().strip().split())
    grafo[origen].append((origen, destino, peso))
    grafo[destino].append((destino, origen, peso))
viaje(grafo)
