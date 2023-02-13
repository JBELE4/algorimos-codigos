def fun(i,visitado,grado,cont):
    if cont>0:
        for z in range (len(grado[i])):
            fun(grado[i][z],visitado,grado,cont-1)
    else:
        if i not in  visitado:
            visitado.add(i)




def isla(grado):
    cont=2
    long=len(grado)
    visitado=set()
    for i in range(long):
        if i not in visitado:
            fun(i,visitado,grado,cont)
            cont=2
    cont=0
    if len(visitado)==long:
        print("bien")
    else:
        print("mal")












n,m=map(int,input().strip().split())
grado=[]
for i in range (n):
    grado.append([])
for i in range(m):
    a,b=map(int,input().strip().split())
    grado[a].append(b)
isla(grado)