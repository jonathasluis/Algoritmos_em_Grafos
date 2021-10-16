"""
Por: Jonathas Luis De Sousa
GCC218 - Algoritmos em Grafos
Departamento de Ciencia da Computacao - DCC
Universidade Federal de Lavras - UFLA
"""


infinito = float('inf') # definindo um valor infinito

class Vertice:
    def __init__(self,v):
        self.valor = v # valor do vertice
        self.d = infinito # distancia até a fonte
        self.pi = None # pai

    '''retorna a distancia'''
    def getD(self): 
        return self.d

class Aresta:
    def __init__(self,u,v,p):
        self.vertices = (u,v) # tupla dos vertices
        self.peso = {self.vertices : p} # aresta, vertices e peso
    
    def get_peso(self,u,v):# retorna o peso de uma aresta
        chave = (u,v)
        return self.peso[chave]

''' inicializa os vertices e armazena em uma lista '''
def inicializar(V):
    listaVertices = []
    for v in V:
        v = Vertice(v)
        listaVertices.append(v)

    listaVertices[0].d = 0
    return listaVertices

def relaxar(u,v,a):
    if v.d > (u.d + a.get_peso(u,v)):
        v.d = u.d + a.get_peso(u,v)
        v.pi = u

'''algoritmo de Dijkstra, recebe uma lista de vertices e uma lista de arestas'''
def dijkstra(V,E): 
    Q = [V[0]]
    S = []
    while Q:
        S.append(Q.pop(0))

        for i in E:
            u = i.vertices[0]
            v = i.vertices[1]

            pai_nulo = False

            if v.pi == None:
                pai_nulo = True
      
            relaxar(u,v,i)

            if pai_nulo and not(v in S): # u ∈ V – S
                Q.append(v)
            else:
                Q = sorted(Q,key = Vertice.getD)

def main():
    vertices,arestas = map(int,input().split()) #entrada |V| e |E|

    V = list(range(1,vertices+1))
    V = inicializar(V) # inicializa os vertices

    # lista de Arestas
    E = []

    x = 0
    while x < arestas:
        u,v,p = map(int,input().split()) # entrada aresta e peso
        u = V[u-1]
        v = V[v-1]
        a = Aresta(u,v,p)
        E.append(a)
        x +=1

    dijkstra(V,E)

    for i in V:
        print('distancia entre 1 e {}'.format(i.valor),': ',i.d)

main()
