def thanos(habitantes_l,amochados_l,comprobar_l):
    amochados_l.sort()
    for i in comprobar_l:
            if bin(habitantes_l,i,0,len(habitantes_l)-1)>=0:
                if bin(amochados_l,i,0,len(amochados_l)-1)>=0:
                    print(":_(")
                else:
                    print(":)")




def bin(lista,numero_abuscar,baja,alta):
    if(baja>alta):
        return -1
    mid=(baja+alta)//2
    if lista[mid]==numero_abuscar:
        return mid
    elif numero_abuscar<lista[mid]:
        return bin(lista,numero_abuscar,baja,mid-1)
    else:
        return bin(lista, numero_abuscar,  mid +1,alta)








habitantes=int(input())
habitantes_l=[]
hola=input().strip().split(" ")
for i in hola:
    habitantes_l.append(int(i))

amochado=int(input())
amochados_l=[]
hola2=input().strip().split(" ")
for i in hola2:
    amochados_l.append(int(i))

comprobar=int(input())
comprobar_l=[]
hola3=input().strip().split(" ")
for i in hola3:
    comprobar_l.append(int(i))
thanos(habitantes_l,amochados_l,comprobar_l)