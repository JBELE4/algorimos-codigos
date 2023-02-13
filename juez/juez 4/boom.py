def principal(grafo,n ,lista_tipos):
    distancia_nodo=[]
    numerotipos=[80000000000000000000000]*len(lista_tipos)
    for z in range (n):
        distancia_nodo.append(dijkstra(grafo,z))
        for w in range(len(distancia_nodo[z])):
            if(lista_tipos[z]==lista_tipos[w]):
                if  distancia_nodo[z][w]>0:
                    if numerotipos[lista_tipos[z]]>distancia_nodo[z][w]:
                        numerotipos[lista_tipos[z]]=distancia_nodo[z][w]
    for _ in numerotipos:
        if (_!=80000000000000000000000):
            print(_, end=" ")


def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, origin):
    n = len(g) - 1
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
    for _ in range(2, len(g)): #Bucle voraz
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)

    return distances



n, m = map(int, input().strip().split())
tipos=[]
tipos = input().strip().split()
lista_tipos=[]
for i in range(len(tipos)):
    lista_tipos.append(int(tipos[i]))
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    origen, destino, peso = map(int, input().strip().split())
    grafo[origen].append((origen, destino, peso))
    grafo[destino].append((destino, origen, peso))

principal(grafo,n ,lista_tipos)

