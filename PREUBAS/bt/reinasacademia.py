def  imprimir(solucion):
     for i in range (len(solucion)):
         for z in range (len(solucion[i])):
             print(solucion[i][z],end=" ")
         print("")



def BT(solucion,etapa ):
    exito=False
    intento=0
    while intento<len(solucion) and not exito:
        if esfactible(solucion,intento,etapa):
            solucion[etapa][intento]="x"
            if(etapa==7):
                exito=True
            else:
                exito=BT(solucion,etapa+1)
            if not exito:
                solucion[etapa][intento] = " "
        intento=intento+1
    return exito




solucion=[]
for i in range(8):
    fila=[""]*8
    solucion.append(fila)
exito=BT(solucion,0)
if  exito:
    imprimir(solucion)
else:
    print("no hay solucion")