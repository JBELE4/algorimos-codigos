def esfactible(maatriz,nuevaposx,neuvaposy,n,intentos):
   if nuevaposx >=0 and nuevaposx <n and neuvaposy>=0 and neuvaposy<n and maatriz[nuevaposx][neuvaposy]=="0":
       return True

   else:
        return  False



def bt (maatriz,xactual,yactual,Crelativa_y,Crelativa_x,n):
    exito=False
    intentos=0
    while intentos <4 and not exito:
        nuevaposx=xactual+Crelativa_x[intentos]
        neuvaposy=yactual+Crelativa_y[intentos]
        if esfactible(maatriz,nuevaposx,neuvaposy,n,intentos):
            maatriz[nuevaposx][neuvaposy]="x"
            if nuevaposx==n-1 and neuvaposy==n-1:
                exito=True
            else:
               exito =bt(maatriz,nuevaposx,neuvaposy, Crelativa_y, Crelativa_x, n)
               if not exito:
                    maatriz[nuevaposx][neuvaposy] = "0"
        intentos+=1
    return  exito














n=int(input())
maatriz=[]
for i in range (n):
    maatriz.append([])
for z in range (n):
    fila=list(input().strip().split())
    for x in fila:
        maatriz[z].append(x)
Crelativa_x=[1,-1,0,0]
Crelativa_y=[0,0,1,-1]
maatriz[0][0]="x"
exito=bt(maatriz,0,0,Crelativa_y,Crelativa_x,n)
cont=0
for i in range(n):
    for z in range(n):
        if maatriz[i][z]=="0":
            cont+=1
if exito and cont==0:
    print("SI")
else:
    print("NO")

