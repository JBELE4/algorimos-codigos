import copy


def mejor(sol1,sol2):
    if sol1['Valor'] > sol2['Valor']:
        mejor=copy.deepcopy(sol1)
    else:
        mejor=copy.deepcopy(sol2)
    return mejor

def esSol(sol,datos,i):
    es=False
    aux=[]
    while i<datos['N']:
        aux.append(datos['peso'][i])
        i+=1
    if aux:
        return min(aux)+sol['Peso']>datos['Wmax']
    else:
        return True
def initSol(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['N']
    sol['Valor'] = 0
    sol['Peso'] = 0
    return sol
def esFactible(sol,i,datos):
    return (sol['Peso']+datos['peso'][i])<=datos['Wmax']
def asignar(sol,i,datos):
    sol['Valor']+=datos['valor'][i]
    sol['Peso']+=datos['peso'][i]
    return sol
def borrar(sol,i,datos):
    sol['Valor'] -= datos['valor'][i]
    sol['Peso'] -= datos['peso'][i]
    return sol
def VAmasterchof(k,sol,mejorsol,datos):
    if esSol(sol,datos,k):
        mejorsol=mejor(sol,mejorsol)
        return mejorsol
    else:
        for i in range(k,datos['N']):
            if esFactible(sol,i,datos):
                sol=asignar(sol,i,datos)
                mejorsol=VAmasterchof(i+1,sol,mejorsol,datos)
                sol=borrar(sol,i,datos)
    return mejorsol

N,Pmax=map(int,input().strip().split())
datos={}
datos['peso']=[]
datos['valor']=[]
datos['N']=N
datos['Wmax']=Pmax
for i in range(N):
    s,p,v=input().strip().split()
    datos['peso'].append(int(p))
    datos['valor'].append(int(v))

sol=initSol(datos)
mejorsol=initSol(datos)
k=0
mejorsol=VAmasterchof(k,sol,mejorsol,datos)
print(mejorsol['Valor'])


