libs


def mejor(candidatos,matriz):
    ratio=-1
    posicon=-1
    for i in candidatos:
        calcualo=matriz[2][i]/matriz[1][i]

        if ratio<calcualo:
            ratio=calcualo
            posicon=i
    return posicon
def esfactible(bestobejt,matriz,riegos):
    if (riegos>=matriz[1][bestobejt]):
        return True
    else:
        return False



def dyv(matriz,riegos):
    longitud=len(matriz[0])
    candidatos=set()

    for i in range(longitud):
        candidatos.add(i)
    while candidatos:
        bestobejt=mejor(candidatos,matriz)
        candidatos.remove(bestobejt)
        if esfactible(bestobejt,matriz,riegos):
            riegos-=matriz[1][bestobejt]

            print(matriz[0][bestobejt],end=" ")
        else:
            if riegos!=0:
                ratio=riegos/matriz[1][bestobejt]
                if ratio>0:
                    riegos-=ratio*matriz[1][bestobejt]
                    print(matriz[0][bestobejt],end=" ")
                    break










n,riesgo_max=map(int,input().strip().split())
matriz=[]
for i in range(3):
    fila=[i]*n
    matriz.append(fila)
for z in range (n):
    nombre,riegos,beneficio=map(str,input().strip().split())
    matriz[0][z]=nombre
    riegos=int(riegos)
    matriz[1][z]=riegos
    beneficio=int(beneficio)
    matriz[2][z] = int(beneficio)
dyv(matriz,riesgo_max)


