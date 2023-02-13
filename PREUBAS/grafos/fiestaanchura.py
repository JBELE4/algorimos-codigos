from collections import deque


def funcion2(visitadso,i,grafo):
    cola=deque()
    cola.append(i)
    while cola:
        aux=cola.popleft()
        for z in grafo[aux]:
            if visitadso[z]==-1:
                visitadso[z]=z
                cola.append(z)





def funcion(n,m,grafo):
    visitadso=[-1]*n
    for i in range (n):
        if visitadso[i]==-1:
            visitadso[i]=i
            funcion2(visitadso,i,grafo)
    for i in range(n):
        if visitadso[i] != -1:
            print(visitadso[i],end=" ")







n,m=map(int,input().strip().split())
grafo=[]
for i in range(n):
    grafo.append([])
for z in range(m):
    a,b=map(int,input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)
funcion(n,m,grafo)