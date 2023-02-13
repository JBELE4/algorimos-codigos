def esfactoble(mejor_objeto,almendra,peso_max):
    reultado=peso_max-almendra['peso'][mejor_objeto]
    if reultado >-1 :
        return  True
    else:
        return False


def best(candidatos,almendra,almendras):
    ratio=-1
    objetofin=-1
    for i in candidatos:
        if ratio<(almendra['valor'][i]/almendra['peso'][i]):
            ratio=(almendra['valor'][i]/almendra['peso'][i])
            objetofin=i
    return objetofin




def voraz(almendras,pruebass,almendra,pruebas):
    for i in  range (pruebass):
        pruebas_objetivo=pruebas['objetivo'][i]
        peso_max=pruebas['pesomax'][i]
        candidatos=set()
        fin=0
        exit=0
        for i in range (almendras):
            candidatos.add(i)

        while candidatos and  exit==0:
            mejor_objeto=best(candidatos,almendra,almendras)
            candidatos.remove(mejor_objeto)
            print("mejor candi:",mejor_objeto)
            factib=esfactoble(mejor_objeto,almendra,peso_max)

            if factib==True:
                peso_max = peso_max - almendra['peso'][mejor_objeto]
                pruebas_objetivo = pruebas_objetivo - almendra['valor'][mejor_objeto]
                if  pruebas_objetivo <=0:
                    fin=1
                    exit =1
            if factib==False:
                procion=peso_max/almendra['peso'][mejor_objeto]
                if procion!=0:
                    pruebas_objetivo=pruebas_objetivo - (almendra['valor'][mejor_objeto])*procion
                    if pruebas_objetivo<=0:
                     fin=1
                else:
                    fin = 0


        if (fin==0):
            print("TOS")
        else:
            print("PUEDE")





almendras,pruebass=map(int,input().strip().split())

almendra={}
almendra['valor']=[]
almendra['peso']=[]
pruebas={}
pruebas['objetivo']=[]
pruebas['pesomax']=[]



for s in range(almendras):
    a, b = map(int, input().strip().split())
    almendra['valor'] .append(a)
    almendra['peso'].append(b)
for s in range(pruebass):
    a, b = map(int, input().strip().split())
    pruebas['objetivo'] .append(a)
    pruebas['pesomax'].append(b)

voraz(almendras,pruebass,almendra,pruebas)