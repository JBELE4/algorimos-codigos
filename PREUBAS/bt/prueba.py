def esfactible(solucion,etapa,intetos):
    return  True


def bt(solucion,etapa):
    exito=False
    intetos=0
    while intetos <len(solucion) and not  exito:
        if esfactible(solucion,etapa,intetos):
            solucion[etapa][intetos]="x"
            if etapa==7:
                exito=True
            else:
               exito=bt(solucion,etapa+1)
            if exito==False:
                solucion[etapa][intetos] = " "
        intetos+=1
    return  exito