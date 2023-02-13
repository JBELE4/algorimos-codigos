def  comprobar(ini,fin,array3,numero):
    if(ini==fin):
        if array3[ini]==numero:
            return ":_("
        else:
            return ":)"
    else:
        mid=(ini+fin)//2
        if numero>array3[mid]:
           return comprobar(mid+1,fin,array3,numero)
        else:
           return comprobar(ini,mid,array3,numero)




def dyv(array1,array2,array3):
    for i in array3:
        if(comprobar(0, len(array1) - 1, array1, i)):
         w = comprobar(0, len(array2) - 1, array2, i)
         print(w)













n=int(input())
fila1=input().strip().split()
array1=[]
for  i in range(n):
    array1.append(int(fila1[i]))




m=int(input())
fila2=input().strip().split()
array2=[]
for  i in range(m):
    array2.append(int(fila2[i]))


p=int(input())
fila3=input().strip().split()
array3=[]
for  i in range(p):
    array3.append(int(fila3[i]))
dyv(array1,array2,array3)

