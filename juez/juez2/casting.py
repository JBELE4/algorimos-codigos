def casting(p, grafo, visitado, recorridofinal):
    if recorridofinal > 0:
        for i in range(len(grafo[p])):
            casting(grafo[p][i], grafo, visitado, recorridofinal-1)
    else:
        if visitado[p]==False:
            visitado[p] =True


def principal(grafo):
    longitud = len(grafo)
    recorridofinal=2
    contador=0
    visitado=[False]*longitud
    for p in  range(longitud):
        casting(p, grafo, visitado, recorridofinal)

    for a in range(longitud):
        if visitado[a]==True:
            contador+=1

    if(contador==longitud):
      return ("CASTING COMPLETO")
    return ("HAY QUE REPETIR")


personas,relaciones = map(int, input().strip().split())
grafo= []
for _ in range(personas):
    grafo.append([])
for _ in range(relaciones):
    a,b = map(int, input().strip().split())
    grafo[a].append(b)

print(principal(grafo))

