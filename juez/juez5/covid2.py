def ordend(e):
    return len(e)

def dyv(compuesto):
    comun= ""
    compuesto.sort(key=ordend)
    if len(compuesto) == 2:
            for i in range(len(compuesto[0])):
                if compuesto[0][i] == compuesto[1][i]:
                    comun += compuesto[0][i]
                    return comun
    elif len(compuesto) < 2:
        comun = compuesto[0]
        return comun

    else:
        mid = len(compuesto) // 2
        izquierda= dyv(compuesto[:mid])
        derecha = dyv(compuesto[mid:])
        if len(izquierda) > len(derecha):
            return derecha
        else:
            return izquierda


n = int(input())
compuesto = []
for a in range(n):
    compuesto.append(input())
comun=dyv(compuesto)
print(comun)