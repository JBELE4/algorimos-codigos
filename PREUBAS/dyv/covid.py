def comprobar(partedr,parteiz):
    cont=0
    while cont<len(parteiz) and cont<len(partedr) and partedr[cont]==parteiz[cont]:
        cont+=1
    return parteiz[:cont]








def dyv(array):
    if(len(array )==1):
        return array[0]
    else:
        medio=(len(array))//2
        parteiz=dyv(array[:medio])
        partedr=dyv(array[medio:])
        return  comprobar(partedr,parteiz)










n=int(input())
array=[]
for a in range (n):
    x=str(input())
    array.append(x)
w=dyv(array)
print(w)
