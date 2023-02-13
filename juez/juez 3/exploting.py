def esfactible(Riesgo_max, bestobejct, datos_cartas):
    if Riesgo_max >= datos_cartas['riesgo'][bestobejct]:
        return True
    return False


def objeto(candidatos, datos_cartas):
    ratio = -1
    obje = -1
    for i in candidatos:
        if ratio < (datos_cartas['beneficio'][i] / datos_cartas['riesgo'][i]):
            ratio = (datos_cartas['beneficio'][i] / datos_cartas['riesgo'][i])
            obje = i
    return obje


def voraz(datos_cartas, nCartas, Riesgo_max):
    candidatos = set()
    for i in range(nCartas):
        candidatos.add(i)
    sol = [0] * len(candidatos)
    fuera=0
    while candidatos and fuera==0:
        bestobejct = objeto(candidatos, datos_cartas)
        candidatos.remove(bestobejct)
        if esfactible(Riesgo_max, bestobejct, datos_cartas):
            Riesgo_max = Riesgo_max - datos_cartas['riesgo'][bestobejct]
            sol[bestobejct] = 1
            print(datos_cartas['nombre'][bestobejct], " ", end="")
        else:
            if Riesgo_max!=0:
                Riesgo_max=Riesgo_max/ datos_cartas['riesgo'][bestobejct]
                sol[bestobejct] = 1
                print(datos_cartas['nombre'][bestobejct], " ", end="")
            fuera=50


nCartas,Riesgo_max=map(int,input().strip().split())
datos_cartas={}
datos_cartas['nombre']=[]
datos_cartas['riesgo']=[]
datos_cartas['beneficio']=[]
for i in range(nCartas):
    a,b,c=map(str,input().strip().split())
    datos_cartas['nombre'].append(a)
    datos_cartas['riesgo'].append(int(b))
    datos_cartas['beneficio'].append(int(c))
voraz(datos_cartas,nCartas,Riesgo_max)