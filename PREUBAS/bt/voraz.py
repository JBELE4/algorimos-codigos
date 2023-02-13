def esfactible(datos,Pmax,aux):
    if Pmax>=datos[1][aux]:
        return  True
    else:
        return  False
def bestobejct(datos,canditadtos):
    mejro=-1
    pos=-1
    for i in canditadtos:
        ratio=datos[2][i]/datos[1][i]
        if ratio>mejro:
            mejro=ratio
            pos=i
    return i




def voraz(datos,Pmax,n):
    canditadtos=set()
    for i in range(n):
        canditadtos.add(i)
    while canditadtos:
        mejor=bestobejct(datos,canditadtos)
        aux=set.pop(mejor)
        if  esfactible(datos,Pmax,aux):
            Pmax-=datos[1][aux]
            


N,Pmax=map(int,input().strip().split())
datos =[]
for i in range(3):
    datos.append([])
for i in range(N):
    s,p,v=input().strip().split()
    datos[0].append(s)
    datos[1].append(int(p))
    datos[2].append(int(v))
sol=[0]*N
a=voraz(datos,Pmax,n)
print(sol)