def esfactible(i,datos,sol,Pmax):
    if Pmax>=datos[1][i]:
        return True
    else:False

def bt(datos,sol,Pmax,N):
    exito=False
    i=0
    while i <8 and not exito:
        if esfactible(i,datos,sol,Pmax):
            sol[i]+=1
            Pmax-=datos[1][i]
            if Pmax==0:
                exito=True
            else:
               exito= bt(datos, sol, Pmax, N)
            if not  exito:
                sol[i]-=1
                Pmax += datos[1][i]
        i+=1
    return exito






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
exito=bt(datos,sol,Pmax,N)
print(sol)