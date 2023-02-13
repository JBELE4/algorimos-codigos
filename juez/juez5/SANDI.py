def cortar(sandia,c ,xinicio,xfin,yinicio,yfin):
    xmedio=(xinicio+xfin)//2
    ymedio=(yinicio+yfin)//2
    contador=0
    if c==0:
        for i in range(xinicio,xfin):
            for z in range(yinicio,yfin):
                contador+=sandia[i][z]
        return contador
    else:
        return min(cortar(sandia,c-1,xinicio,xmedio,yinicio,ymedio),cortar(sandia,c-1,xinicio,xmedio,ymedio,yfin),cortar(sandia,c-1,xmedio,xfin,yinicio,ymedio),cortar(sandia,c-1,xmedio,xfin,ymedio,yfin))




n,c =map(int,input().strip().split())
sandia=[]
for i in range (n):
    fila=list(map(int, input().strip().split()))
    sandia.append(fila)
a=cortar(sandia,c,0,len(sandia),0,len(sandia))
print(a)