
def select_min_distance(distances, visited):
    min_dist = float('inf')
    best_item = 0
    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            best_item = i
    return best_item


def imprimirPanta (imprimir,total):
    print(total)
    for i in imprimir:
        print(i,end=" ")




def dijkstra(grafo, empiece, final):
    n = len(grafo)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[empiece] = 0
    recorrido=[-1]*n



    for i in range(n - 1):
        nextNode = select_min_distance(distances, visited)
        visited[nextNode] = True
        for m in range(n):
            if not visited[m] and grafo[nextNode][m] != -1:
                distancias=min(distances[nextNode] + grafo[nextNode][m],distances[m])
                if distancias!=distances[m]:
                    distances[m]=distancias
                    recorrido[m] = nextNode
    z=final
    imprimir=[]
    while z !=empiece:
        imprimir.append(recorrido[z])

        z=recorrido[z]
    imprimir.reverse()
    imprimir.append(final)
    imprimirPanta(imprimir, distances[final])


n, m = map(int, input().strip().split())

grafo=[]
a=[]

for i in range(n):
    for j in range(n):
       a.append(-1)
    grafo.append(a)
    a=[]

for i in range(m):
    c1, c2, d = map(int, input().strip().split())
    grafo[c1][c2] = d
    grafo[c2][c1] = d


s, e = map(int, input().strip().split())
dijkstra(grafo, s, e)

