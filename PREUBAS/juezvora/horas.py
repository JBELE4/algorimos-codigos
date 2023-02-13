def mejor(candidatos,n,matriz):
    posicon=5000000000000000000000000
    rat=-1
    for i in candidatos:
        if posicon>matriz[2][i]:
            posicon=matriz[2][i]
            rat=i
    return rat

def esfactible(matriz,best,solucion):
    if solucion==[]:
        return  True
    else:
        longitud=len(solucion)
        if (matriz[1][best]>matriz[2][solucion[longitud-1]]):
            return True
        else:
            return False


def dyv(matriz,n):
    candidatos=set()
    solucion=[]
    for i in range(n):
        candidatos.add(i)
    contador=0
    while candidatos:
        best=mejor(candidatos,n,matriz)
        candidatos.remove(best)
        if esfactible(matriz,best,solucion):
            solucion.append(best)
            contador+=1
    return  contador








n=int(input())
matriz=[]
for i in range (3):
    fila=[i]*n
    matriz.append(fila)


for i in range(n):
    nombre,ini,fin=map(str,input().strip().split())
    matriz[0][i]=nombre
    matriz[1][i] =int(ini)
    matriz[2][i] =int(fin)
print(dyv(matriz,n))