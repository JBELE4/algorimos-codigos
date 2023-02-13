def esfactible(TamañoCesta, bestobejct, alimento):
    if TamañoCesta >= alimento['tamaño'][bestobejct]:
        return True
    return False


def objeto(candidatos, alimento):
    ratio = -1
    obje = -1
    for i in candidatos:
        if ratio < (alimento['beneficio'][i] / alimento['tamaño'][i]):
            ratio = (alimento['beneficio'][i] / alimento['tamaño'][i])
            obje = i
    return obje


def voraz(alimento, nAlimentos, TamañoCesta):
    candidatos = set()
    for i in range(nAlimentos):
        candidatos.add(i)
    sol = [0] * len(candidatos)
    fuera=0
    resutaldo = 0
    while candidatos and fuera==0:
        bestobejct = objeto(candidatos, alimento)
        candidatos.remove(bestobejct)

        if esfactible(TamañoCesta, bestobejct, alimento):
            TamañoCesta = TamañoCesta - alimento['tamaño'][bestobejct]
            resutaldo=resutaldo+alimento['beneficio'][bestobejct]

        else:
            proporcion=TamañoCesta/alimento['tamaño'][bestobejct]
            if proporcion!=0:
                    resutaldo=resutaldo+((alimento['beneficio'][bestobejct])*proporcion)


            fuera=50
    print("%.6f"%resutaldo)


nAlimentos,TamañoCesta=map(int,input().strip().split())
alimento={}
alimento['nombre']=[]
alimento['tamaño']=[]
alimento['beneficio']=[]
for i in range(nAlimentos):
    a,b,c=map(str,input().strip().split())
    alimento['nombre'].append(a)
    alimento['tamaño'].append(float(b))
    alimento['beneficio'].append(float(c))
voraz(alimento,nAlimentos,TamañoCesta)