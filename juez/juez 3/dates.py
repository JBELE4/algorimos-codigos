def elMejor(candidatos, grupoMan, persona):
    bestitem=-1
    edad=8000000000000
    for i in candidatos:
        if edad>persona['edad'][i]:
            edad=persona['edad'][i]
            bestitem=i
    return bestitem



def esfactible(bestobject, grupoMan, cont):
    if cont>0:
        return True

    return False


def voraz(participantes, grupoMan, persona):
    candidatos=set()
    contador=-1
    operacion=0

    operacion=participantes-grupoMan
    if (operacion>grupoMan):
        contador=grupoMan
    else:
        contador=operacion

    for i in  range (participantes):
        candidatos.add(i)
    while candidatos:
         bestobejct=elMejor(candidatos, grupoMan, persona)
         candidatos.remove(bestobejct)
         if esfactible(bestobejct, grupoMan,contador):
                contador-=1
                print(persona['nobre'][bestobejct],end=" ")
         else:
             if contador ==0:
                 print("")
                 contador=-1
             print(persona['nobre'][bestobejct], end=" ")









participantes, grupoMan = map(int, input().strip().split())
persona = {}
persona['nobre'] = []
persona['edad'] = []
for _ in range(participantes):
    nombre, edad = map(str, input().strip().split())
    persona['nobre'].append(nombre)
    persona['edad'].append(int(edad))
voraz(participantes, grupoMan, persona)
