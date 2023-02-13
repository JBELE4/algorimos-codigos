


def esSolucion(N,k,visitado,tablero):
    if k==(N*N)-1:
        es=True
        aux=0
        fila = aux // len(tablero)
        columna = aux % len(tablero)
        while es and aux<len(visitado):
            fila = aux // len(tablero)
            columna = aux % len(tablero)
            if visitado[aux]==False and tablero[fila][columna]==0:
                es=False
            aux+=1
        return es
    else:
        return False
def esFactible(N,k,visitado,tablero):
    fila = k // len(tablero)
    columna = k % len(tablero)
    return k>=0 and k<(N*N) and tablero[fila][columna]==0 and visitado[k]==False
def VAfindaway(N,k,visitado,tablero):
    global limite
    if not limite:
        if esSolucion(N,k,visitado,tablero):
            print("SI")
            limite=True
        else:
            if k%len(tablero)!=N-1:
                if esFactible(N,k+1,visitado,tablero):
                    visitado[k + 1] = True
                    VAfindaway(N,k+1,visitado,tablero)
                    visitado[k + 1] = False
            if k%len(tablero)!=0:
                if esFactible(N,k-1,visitado,tablero):
                    visitado[k - 1] = True
                    VAfindaway(N,k-1,visitado,tablero)
                    visitado[k - 1] = False
            if esFactible(N,k+N,visitado,tablero):
                visitado[k + N] = True
                VAfindaway(N,k+N,visitado,tablero)
                visitado[k+N]=False
            if esFactible(N,k-N,visitado,tablero):
                visitado[k - N] = True
                VAfindaway(N,k-N,visitado,tablero)
                visitado[k-N]=False


N=int(input())
tablero=[]
k=0
visitado=[False]*(N*N)
##for i in range(N):
  ##  tablero.append([])
for i in range(N):
    tablero.append(list((map(int,input().strip().split()))))
limite=False
visitado[0]=True
answer=VAfindaway(N,k,visitado,tablero)
if not limite:
    print("NO")