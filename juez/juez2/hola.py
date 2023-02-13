from collections import  deque



def pilotes(i,grafo,visitados):
  candidatos=deque()
  visitados[i]=True
  candidatos.append(i)
  while candidatos:
      aux =candidatos.popleft()
      for z in grafo[aux]:
          if visitados[z]==False:
              visitados[z]=True
              candidatos.append(z)





def principal(grafo):
    n=len(grafo)
    visitados=[False]*n
    cont=0
    for i in range (n):
        if visitados[i]==False:
            pilotes(i,grafo,visitados)
            cont+=1
    return cont


personas,relaciones=map(int,input().strip().split())
grado=[]
for i in range (personas):
    grado.append([])
for W in range (relaciones):
    a,b=map(int,input().strip().split())
    grado[a].append(b)
    grado[b].append(a)
print(principal(grado))