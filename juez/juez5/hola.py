def ordenar(e):
    return len(e)

def buscarcomun(der,izq):
    contador=0
    while contador < len(der)and contador< len(izq)and izq[contador] == der[contador]:
        contador+=1
    return izq[:contador]





def dyv(compuesto):
    if len(compuesto)>1:
        medio=len(compuesto)//2
        derecha=dyv(compuesto[medio:])
        izquierda=dyv(compuesto[:medio])
        return buscarcomun(derecha,izquierda)

    elif len(compuesto)==1:
        return  compuesto[0]






n = int(input())
compuesto = []
for a in range(n):
    compuesto.append(input())
compuesto.sort(key=ordenar)
comun=dyv(compuesto)
print(comun)
