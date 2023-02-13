def esfactbible(selecionados,besttobejct,horas,cont):
    if selecionados[0]==False:
        if cont==0:
            return True
        else:
             if(horas['inicio'][besttobejct]>horas['fin'][cont-1]):
                return True
             else:
                return False





def mejor(candidatos,horas):
    besthora=800000000000000000
    bestitem=-1
    for i in candidatos:
        if(besthora>horas['fin'][i]):
            besthora=horas['fin'][i]
            bestitem=i
    return bestitem
def pricipal(a,horas):
    candidatos=set()
    selecionados=[False]*a
    cont=0
    fin=0
    for i in range (a):
        candidatos.add(i)
    while candidatos:

        besttobejct=mejor(candidatos,horas)
        candidatos.remove(besttobejct)
        if esfactbible(selecionados,besttobejct,horas,cont):
            selecionados[cont]=True
            cont+=1
    for z in range(len(selecionados)):
        if (selecionados[z]==True):
            fin+=1


    print(fin)
a=int(input( ))
horas={}
horas['nombre']=[]
horas['inicio']=[]
horas['fin']=[]
for i in range(a):

    b,c,d=map(str,input().strip().split())
    horas['nombre'].append(b)
    horas['inicio'].append(int(c))
    horas['fin'].append(int(d))
pricipal(a,horas)