from  collections import  deque

def comprobar_re(v,g,visitados):
    relaciones=deque()
    visitados[v]=True
    relaciones.append(v)
    while relaciones:
        aux=relaciones.popleft()
        for adj in g[aux]:
            if not visitados[adj]:
                visitados[adj]=True
                relaciones.append(adj)




def prrincipal(g):
    visitados=[False]*len(g)
    for v in range (len(g)):
        if not  visitados[v]:
            comprobar_re(v,g,visitados)





asistente,relaciones=map(int,input().strip().split())
grafo=[]
a,b=map(int,input().strip().split())
grafo[a].append(b)
grafo[b].append(a)
prrincipal(g)