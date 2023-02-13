
def combinar(resultado2,resultado1):
 resultado=resultado1 and resultado2
 return  resultado



def cifras(numero):
    resultado=[False]*10
    while (numero>0):
       resto = numero % 10
       numero= numero//10
       resultado[resto]=True
    return  resultado

def dyv(numero,ini,fin):
    if ini==fin:
        return cifras(numero[ini])
    else:
        mitad=(ini+fin)//2
        resultado1=dyv(numero,ini,mitad)
        resultado2 = dyv(numero, mitad+1,fin)
        resultado=combinar(resultado2,resultado1)
        return resultado









numero=[123,85612,5612]
a=dyv(numero,0,len(numero)-1)
print(a)
for i in range(9):
    if a[i]==True:
        print(i)