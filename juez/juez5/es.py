
def comprobar(compueto, acomprobar):
    varible = False
    for i in compueto:
        if i.find(acomprobar) > -1:
            varible = True
        else:
            varible = False
    return varible

def dyv (compuesto):
    compuesto.sort(key=len)
    fin=""
    for i in compuesto[0]:
        if comprobar(compuesto,i):
            fin=fin+i
    return fin

n = int(input())
compuesto = []
for a in range(n):
    compuesto.append(input())
comun=dyv(compuesto)
print(comun)