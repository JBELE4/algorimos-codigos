
def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
        candidates.sort()
    return candidates

def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id



def kruskal(g):
    candidates = sortCandidates(g)
    components = list(range(len(g)))
    count = len(components)
    sol = 0
    i = 0
    while count > 1 and len(candidates) > i:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
        i += 1

    if(sol%5)==0:
        return (sol /5)
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
print(kruskal (grafo))
