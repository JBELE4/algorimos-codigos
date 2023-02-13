def esfactible(best,almendra,pruebas,peso):
    if peso>=almendra['peso'][best]:
        return True
    return  False
def mejor(candidatos,almendra):
    ratio=-1
    merjor=-1
    caculo=-1
    for i in  candidatos:
        caculo=(almendra['valor'][i]/almendra['peso'][i])
        if ratio<caculo:
            ratio=caculo
            merjor=i
    return  merjor




def voraz(numeroAL,pruebasT,almendra,pruebas):
    for z in  range(pruebasT):
        peso=pruebas['pesoMax'][z]
        valor= pruebas['valorNu'][z]
        candidatos=set()
        for i in  range(numeroAL):
            candidatos.add(i)
        while candidatos:
            best=mejor(candidatos,almendra)
            candidatos.remove(best)
            if esfactible(best,almendra,pruebas,peso):
                peso=peso-almendra['peso'][best]
                valor=valor-almendra['valor'][best]
            else:
                proporcion=peso/almendra['peso'][best]
                if (proporcion!=0):
                    peso=peso-proporcion*almendra['peso'][best]
                    valor = valor - almendra['valor'][best]*proporcion

        if valor<=0 and peso >=0:
            print("PUEDE")
        else:
            print("TOS")









numeroAL,pruebasT=map(int,input().strip().split())

almendra={}
almendra['valor']=[]
almendra['peso']=[]
for _ in range (numeroAL):
    a,b=map(int,input().strip().split())
    almendra['valor'].append(a)
    almendra['peso'].append(b)
pruebas={}
pruebas['valorNu']=[]
pruebas['pesoMax']=[]
for _ in range (pruebasT):
    a,b=map(int,input().strip().split())
    pruebas['valorNu'].append(a)
    pruebas['pesoMax'].append(b)
voraz(numeroAL,pruebasT,almendra,pruebas)