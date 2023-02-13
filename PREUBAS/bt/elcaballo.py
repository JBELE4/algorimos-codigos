def esfactible(n,m,p,array,nX,nY,abuscar):



    if (nX>=0 and nX<n and nY<m and nY >=0 ):
        w=array[nX][nY]
        if abuscar==1 and w!="x" and w==0:
            return True
        if w!="x" and w==abuscar  :
             return True
        else:
            return False
    else:
        return  False

def bt(array,contador,p,n,m,aux_y,aux_x,posicionx,posciony,abuscar):
    exito=False
    intento=0
    while intento<=3 and not  exito:
        nX=posicionx+aux_x[intento]
        nY=posciony+aux_y[intento]
        if esfactible(n,m,p,array,nX,nY,abuscar+1):
            array[posicionx][posciony]="x"
            contador+=1
            if (abuscar+1==p):
                exito=True
            else:
               exito= bt(array,contador,p,n,m,aux_y,aux_x,nX,nY,abuscar+1)
            if not exito:
                array[nX][nY] = abuscar
                contador-=1
        intento+=1


n,m,p=map(int,input().strip().split())
array=[]
for i in range(n):
    array.append([])

for i in range(n):
    a=input().strip().split()
    for z in range(m):
        array[i].append(int(a[z]))
aux_y=[1,-1,0,0]
aux_x=[0,0,1,-1]
print(array)
contador=1
array[0][0]="x"
bt(array,contador,p,n,m,aux_y,aux_x,0,0,1)
print(contador)
print(array)