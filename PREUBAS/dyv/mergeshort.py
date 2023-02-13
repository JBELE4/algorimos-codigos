def dyv(vetor,ini,fin):
    if (ini==fin):
        return vetor[ini]
    else:
        medio=(ini+fin)//2
        lado1=dyv(vetor,ini,medio)
        lado2=dyv(vetor,medio+1,fin)
        resultado=0
        if lado2>lado1:
            resultado=lado2
        else:
            resultado=lado1
        return resultado










vetor=[10,20,80,90,1,5555,6]
ini=0
fin=len(vetor)-1
print(dyv(vetor,ini,fin))