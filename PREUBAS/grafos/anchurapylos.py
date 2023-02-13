from collections import deque


def funcion(visitados,i,n,grafo):
    cola=deque()
    visitados[i]=True
    cola.append(i)
    while cola:
        auxiliar=cola.popleft()
        for z in grafo[auxiliar]:
            if visitados[z]==False:
                visitados[z]=True
                cola.append(z)





def grafos(n,m,grafo):
    visitados=[False]*n
    contado=0
    for i in range (n):
        if visitados[i]==False:
            funcion(visitados,i,n,grafo)
            contado+=1
    return contado













n,m=map(int,input().strip().split())
grafo=[]
for z in range (n):
    grafo.append([])
for i in range(m):
    a,b=map(int,input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)
print(grafo)
print(grafos(n,m,grafo))