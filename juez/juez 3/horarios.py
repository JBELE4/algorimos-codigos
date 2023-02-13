def mejorActividad(activida,actividades_max,conjunto):
    mejor=-1
    tiempo=80000000000000
    for i in conjunto:
        if tiempo>activida['fin'][i]:
            tiempo=activida['fin'][i]
            mejor=i
    return mejor
def factible(sol,mejora,activida):
    for i in  range (len(sol)):
        if sol[i]==-1:
            if i==0:
                return  True
            else:
                w=sol[i-1]
                if activida['inicio'][mejora] < activida['fin'][w]:
                    return False
                else:
                   return True






def voraz(activida,actividades_max):
    conjunto=set()
    cont=0
    cont2=0
    for i in range(actividades_max):
        conjunto.add(i)
    sol=[-1]*actividades_max
    while conjunto:
        mejora=mejorActividad(activida,actividades_max,conjunto)
        conjunto.remove(mejora)
        if factible(sol,mejora,activida):
            sol[cont2]=mejora
            cont2+=1

    for i in range (len(sol)):
        if sol[i] !=-1:
            cont=cont+1
    print(cont)


actividades_max=int(input())
activida={}
activida['nombre']=[]
activida['inicio']=[]
activida['fin']=[]
for i in range (actividades_max):
    nombre,inicio,fin = map(str, input().strip().split())
    activida['nombre'].append(nombre)
    activida['inicio'].append(int(inicio))
    activida['fin'].append((int(fin)))
voraz(activida,actividades_max)