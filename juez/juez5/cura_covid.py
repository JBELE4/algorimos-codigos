def prefijo_comun(izq, der):
    i = 0
    while i < len(izq) and i < len(der) and izq[i] == der[i]:
        i += 1
    return izq[:i]


def covid(molecular):
    if len(molecular) == 1:
        return molecular[0]
    else:
        mitad = len(molecular) // 2
        izq = covid(molecular[:mitad])
        der = covid(molecular[mitad:])
        return prefijo_comun(izq, der)


n = int(input(""))
molecular = []

for i in range(n):
    c = input("")
    molecular.append(c)

print(covid(molecular))

'''
5 
CHOS 
C
CO 
CH 
CC
'''
