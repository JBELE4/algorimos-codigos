from collections import deque


def funci(visitado,grafo,n,i):
    visitado[i]=True
    cola=deque()
    cola.append(i)
    while cola:
        aux=cola.popleft()
        for z in grafo[aux]:
            if visitado[z]==False:
                visitado[z] = True

                cola.append(z)




def grafos(n,m,grafo):
    visitado=[False]*n
    cont=0
    for i in range(n):
        if visitado[i]==False:
            funci(visitado,grafo,n,i)
            cont+=1
    print(cont)












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