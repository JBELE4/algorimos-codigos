def ordend(e):
    return len(e)


def dyv(compuesto):
    if len(compuesto) <= 2:
        common_prefix = ""

        shortest_string = min(compuesto, key=len)
        if len(compuesto) == 2:
            for i in range(len(shortest_string)):
                if compuesto[0][i] == compuesto[1][i]:
                    common_prefix += compuesto[0][i]

        else:
            common_prefix = compuesto[0]
        return common_prefix



    else:
        medio = len(compuesto) // 2
        izquierda = dyv(compuesto[:medio])
        derecha = dyv(compuesto[medio:])
        if len(izquierda) > len(derecha):
            return derecha
        elif len(izquierda) == len(derecha):
            return izquierda
        else:
            return izquierda


n = int(input())
compuesto = []
for a in range(n):
    compuesto.append(input())
comun=dyv(compuesto)
print(comun)
