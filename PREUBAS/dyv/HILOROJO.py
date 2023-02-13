def  estar(array,inicio,fin,numero):

    if inicio==fin:
        if (array[inicio]==numero):
            return True
        else:
            return False
    else:
        medio=(inicio+fin)//2
        if numero>array[medio]:
           return estar(array, medio+1, fin, numero)

        else:
            return estar(array, inicio,medio, numero)



def dyv(array1,array2,compro):

    for i in  range (len(compro)):
        if estar(array1,0,len(array1)-1,compro[i][0]) and estar(array2,0,len(array2)-1,compro[i][1]):
            print(array1.index(compro[i][0])," ",array2.index(compro[i][1]))
        else:
            print("SIN DESTINO")

















n=int(input())
array1=[]
fila1=input().strip().split()
for i in fila1:
    array1.append(int(i))

m=int(input())
array2=[]
fila2=input().strip().split()
for i in fila2:
    array2.append(int(i))
p=int(input())
compro=[]
for i in range(p):
    compro .append([])

for i in range(p):
    a,b=map(int,input().strip().split())
    compro[i].append(a)
    compro[i].append(b)

dyv(array1,array2,compro)