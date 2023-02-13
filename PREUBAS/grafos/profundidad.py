def  func(grado,i,long,longitudma,fuer):
    if longitudma>0:
        for z in range (len(grado[i])):
            func(grado, grado[i][z], long, longitudma-1, fuer)

    else:
        if fuer[i]==False:
            fuer[i]==True







def isla(grado):
    long=len(grado)
    fuer=[False]*long
    longitudmax=2
    for i in range (long):
        if fuer[i]==False:
            func(grado,i,long,longitudmax,fuer)
            longitudmax=2


    cont=0
    for x in fuer:
        if x!=False:
            cont+=1
    if cont==long:
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