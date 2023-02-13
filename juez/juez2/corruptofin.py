
def comprobrar(p,visitado,grafo):
    final=False
    if visitado[p]==False :
        visitado[p]=True
        for a in range(len(grafo[p])):
            final=comprobrar(grafo[p][a],visitado,grafo)

    else:
        final=True
    return final


def corrupcion(grafo):
    longitud=len(grafo)
    terminar=False
    visitado=[False]*longitud
    for p in  range(longitud):
        terminar=comprobrar(p,visitado,grafo)
        visitado=[False]*longitud
        if terminar == True:
          break

    if terminar==True:
        return "CORRUPTOS"
    else:
        return "INOCENTES"



personas,relaciones = map(int, input().strip().split())
grafo= []
for _ in range(personas):
    grafo.append([])
for _ in range(relaciones):
    a,b = map(int, input().strip().split())
    grafo[a].append(b)

print(corrupcion(grafo))





