from collections import deque
def pylotes(p,visitado,grafo):
    cola = deque()
    visitado[p] = True
    cola.append(p)
    while cola:
        auxiliar = cola.popleft()
        for a in grafo[auxiliar]:
            if visitado[a] == False:
                visitado[a] = True
                cola.append(a)


def principal(grafo):
    contador = 0
    longitud = len(grafo)
    visitado = [False] * longitud
    for p in range(longitud):
        if visitado[p] == False:
            pylotes(p,visitado,grafo)
            contador += 1
    return contador

asistentes, relaciones = map(int, input().strip().split())
grafo = []
for _ in range(asistentes):
    grafo.append([])
for _ in range(relaciones):
    a, b = map(int, input().strip().split())
    grafo[a].append(b)
    grafo[b].append(a)
print(principal(grafo))
