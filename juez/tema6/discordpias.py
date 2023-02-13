

def esFactible(grafo,solucion,nodo,modelo):
    esFac=True
    adj=0
    while esFac and adj < len(grafo[nodo]):
        aux=grafo[nodo][adj]
        esFac= solucion[aux]!= modelo
        adj+=1
    return esFac

def esSolucion(nodo,N):
    si=True
    i=0
    while si and i<N:
        if solucion[i]==0:
            si=False
        i+=1
    return si

def VAdiscordpias(grafo,N,solucion,nodo,nummodelo):
    if esSolucion(nodo,N):
        esSol=True
        print(max(solucion))
    else:
        esSol=False
        modelo=1
        while not esSol and modelo<=nummodelo:
            if esFactible(grafo,solucion,nodo,modelo):
                solucion[nodo]=modelo
                esSol,solucion=VAdiscordpias(grafo,N,solucion,nodo+1,nummodelo)
                if not esSol:
                    solucion[nodo]=0
            modelo+=1
    return esSol,solucion


N,M=map(int,input().strip().split())
grafo=[]
for i in range(N):
    grafo.append([])
for i in range(M):
    u,v=map(int,input().strip().split())
    grafo[u].append(v)
    grafo[v].append(u)
modelo=1
solucion=[0]*N
nodo=0
esSol=False
nummodelo=-1
while not esSol:
    nummodelo+=1
    esSol,modelos=VAdiscordpias(grafo,N,solucion,nodo,nummodelo)

