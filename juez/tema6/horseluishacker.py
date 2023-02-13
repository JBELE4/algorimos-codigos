def esSolucion(lastitem,P):
    return lastitem==P
def hayobjeto(lastitem,mapa,k):
    fila = k // M
    columna = k % M
    return mapa[fila][columna]==lastitem+1
def esFactible(visitados,N,mapa,k,lastitem,P):
    fila = k // M
    columna = k % M
    return k>=0 and k<(N*M) and mapa[fila][columna]<=P and (mapa[fila][columna]==0 or mapa[fila][columna]==lastitem+1) and  not visitados[k]

def VAhorseluis(visitados,N,M,P,mapa,lastitem,soluciones,contador,k):
    fila = k // M
    columna = k % M
    if esSolucion(lastitem,P):
        soluciones.append(contador)
        return soluciones
    else:
        if k % M != M - 1:
            if esFactible(visitados,N,mapa,k+1,lastitem,P):
                visitados[k+1]=True
                if hayobjeto(lastitem,mapa,k+1):
                    lastitem += 1
                    contador+=1
                    soluciones=VAhorseluis(visitados,N,M,P,mapa,lastitem,soluciones,contador,k+1)
                    contador-=1
                    lastitem-=1
                else:
                    contador += 1
                    soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k + 1)
                    contador -= 1
                visitados[k + 1] = False
        if k % M != 0:
            if esFactible(visitados,N,mapa,k-1,lastitem,P):
                visitados[k - 1] = True
                if hayobjeto(lastitem,mapa,k-1):
                    lastitem += 1
                    contador += 1
                    soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k -1)
                    contador -= 1
                    lastitem-=1
                else:
                    contador += 1
                    soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k - 1)
                    contador -= 1
                visitados[k - 1] = False
        if esFactible(visitados,N,mapa,k+M,lastitem,P):
            visitados[k + M] = True
            if hayobjeto(lastitem,mapa,k+M):
                lastitem += 1
                contador += 1
                soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k + M)
                contador -= 1
                lastitem -=1
            else:
                contador += 1
                soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k + M)
                contador -= 1
            visitados[k + M] = False
        if esFactible(visitados,N,mapa,k-M,lastitem,P):
            visitados[k - M] = True
            if hayobjeto(lastitem,mapa,k-M):
                lastitem += 1
                contador += 1
                soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k - M)
                contador -= 1
                lastitem-=1
            else:
                contador += 1
                soluciones=VAhorseluis(visitados,N, M, P, mapa, lastitem, soluciones, contador, k - M)
                contador -= 1
            visitados[k-M]= False
    return soluciones


N,M,P=map(int,input().strip().split())
mapa=[]
for i in range(N):
    mapa.append(list(map(int,input().strip().split())))
k=0
limite=False
contador=1
soluciones=[]
lastitem=0
visitados=[False]*N*M
visitados[0]=True
test=VAhorseluis(visitados,N,M,P,mapa,lastitem,soluciones,contador,k)
print(min(test))
