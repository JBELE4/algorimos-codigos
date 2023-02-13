def bestobejct(candiatos,a):
    maximo=-1
    pos=-1
    for z in  candiatos:
        op=a["valor"][z]/a["peso"][z]
        if maximo<op:
            maximo=op
            pos=z
    return pos
def esfacctible(mejor,maximoPeso,a):

    maximoPeso -= a["peso"][mejor]
    if maximoPeso>-1:
            return True
    else:
        return False


def funcion(x, y, a):
    maximaValro=x
    maximoPeso=y
    candiatos=set()
    fin=-1
    for i in range (len(a["peso"])):
        candiatos.add(i)
    while candiatos and fin==-1:
        mejor=bestobejct(candiatos,a)
        candiatos.remove(mejor)
      


        if esfacctible(mejor,maximoPeso,a):
            maximoPeso-=a["peso"][mejor]
            maximaValro-=a["valor"][mejor]
            if(maximaValro<=0):
                return "PUEDE"

        else:
                ratio=maximoPeso/a["peso"][mejor]
                if(ratio!=0):
                    maximaValro -= (a["valor"][mejor] * ratio)
                    maximoPeso-=(a["peso"][mejor]*ratio)
                    if (maximaValro <= 0):
                        return "PUEDE"
    return "TOS"







n,m=map(int,input().strip().split())
a={}
a["peso"]=[]
a["valor"]=[]
for i in range (n):

    v,p=map(int,input().strip().split())
    a["peso"].append(p)
    a["valor"].append(v)
for z in  range(m):
    x, y = map(int, input().strip().split())
    print(funcion(x,y,a))





