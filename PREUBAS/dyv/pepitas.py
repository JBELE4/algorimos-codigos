def dyv(matriz,xini,xfin,yini,yfin,contador):

    if (contador==0):
        peptitas = 0
        for i in range (xini,xfin):
            for z in range (yini,yfin):
                peptitas+=int(matriz[i][z])

        return peptitas

    mediox=(xini+xfin)//2
    medioY=(yini+yfin)//2
    resultado1=dyv(matriz,mediox,xfin,yini,medioY,contador-1)
    resultado2 = dyv(matriz, xini, mediox, yini,medioY, contador - 1)
    resultado3 = dyv(matriz,mediox,xfin, medioY, yfin, contador - 1)
    resultado4 = dyv(matriz, xini, mediox, medioY, yfin ,contador - 1)
    return min(resultado4,resultado3,resultado2,resultado1)


n,c=map(int,input().strip().split())
matriz=[]
for i in range(n):
    fila=input().strip().split()
    matriz.append(fila)
a=dyv(matriz,0,n,0,n,c)
print(a)