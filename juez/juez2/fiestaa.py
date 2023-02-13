from collections import deque


def principal(grafo):
    lista_formato = []
    longitud = len(grafo)
    visitado = [False] * longitud
    for p in range(longitud):
        if visitado[p] == False:
            lista_formato = relacion(p, grafo, visitado)

            for n in range(len(lista_formato)):
                print(lista_formato[n], end=" ")


def relacion(p, grafo, visitado):
    cola = deque()
    lista_resultado = []
    visitado[p] = True
    cola.append(p)
    lista_resultado.append(p)
    while cola:
        auxiliar = cola.popleft()
        for a in grafo[auxiliar]:
            if visitado[a] == False:
                visitado[a] = True
                cola.append(a)
                lista_resultado.append(a)

    lista_resultado.sort()
    return lista_resultado


asistentes, relaciones = map(int, input().strip().split())
grafo = []
for _ in range(asistentes):
    grafo.append([])
for _ in range(relaciones):
    a, b = map(int, input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)
principal(grafo)
