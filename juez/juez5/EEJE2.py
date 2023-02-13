import time


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






def recBinarySearch(v, number):


    return bin(v, number, 0, len(v) - 1)






a=int(input())
fila1=[]
hola=input().strip().split(" ")
for i in hola:
    fila1.append(int(i))



b=int(input())
fila2=[]
hola2=input().strip().split(" ")
for z in hola2:
    fila2.append(int(z))


c=int(input())
aux1=-1
aux2=-1
primero=[]
segundo=[]

for m in range (c):
    a, b = map(int, input().strip().split())
    aux1 = recBinarySearch(fila1, int(a))
    aux2 = recBinarySearch(fila2, int(b))
    if aux1==-1 or aux2 ==-1:
        print("SIN DESTINO")
    else:
        print(aux1,aux2)

















