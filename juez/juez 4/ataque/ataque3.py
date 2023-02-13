from random import randint
def selectMin(candidates, visited):
    vertex= None
    weight= float('inf')
    for i in range(0,len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex=i
            weight=candidates[i]
    return vertex,weight

def prim(g):
    n=len(g)
    initial=0
    visited=[False]*n
    sol=0
    visited[initial]=True
    candidates=[float('inf')]*n
    for (start, end, weight) in g[initial]:
        candidates[end]=weight
    for i in range(1,n):
        nextNode, cost = selectMin(candidates, visited)
        if cost<float('inf'):
            sol+=cost
            visited[nextNode]=True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end]= min(weight, candidates[end])

    if sol%5==0:
        return (sol//5)
    else:
        return (sol//5)+1




n, m = map(int, input().strip().split())
grafo = []
for i in range(n):
    grafo.append([])
for i in range(m):
    origen, destino, peso = map(int, input().strip().split())
    grafo[origen].append((origen, destino, peso))
    grafo[destino].append((destino, origen, peso))
print(prim(grafo))

