# -*- coding: utf-8 -*-
''' 
Por: Felipe de Oliveira Fernandes e Jonathas Luis de Sousa
GCC218 - Algoritmos em Grafos
Turma: 10A
Universidade Federal de Lavras - UFLA
'''

'''
1152 - Estradas Escuras
O problema apresenta um grafo, que os vertices são o número de junções, as arestas as estradas e
os pesos das arestas são as medidas em metros das estradas. O Governo da cidade quer reduzir o custo
eles querem otimizar o sistema de tal forma que após desligar a iluminação de algumas estradas à noite,
sempre existirá algum caminho iluminado de qualquer junção de Byteland para qualquer outra junção.

Solução: para resolver esse problema utilizamos o algoritmo de Kruskall, que por meio de um grafo,
ele gera uma arvore com o menor custo, em relação aos pesos das arestas. 
Assim para calcular a economia basta realizar a difença entre o custo antes e depois da AGM.
'''

'''
Recebe dois conjuntos (subarvores) e 
efetua a uniao entre as duas estruturas
'''
def uniao(x, y, conjuntos):
    ligar(x, y, conjuntos)
    
'''
Concatena as duas subarvores,
atualizando seus pais e seu rank
    conjuntos[v][0]: pai do vertice v
    conjuntos[v][1]: rank do vertice v
'''    
def ligar(x, y, conjuntos):
    # Se a subarvore x eh maior que a subarvore y, x passa a ser pai de y
    if(conjuntos[x][1] > conjuntos[y][1]):
        conjuntos[y][0] = x
    else: # Caso contrario, y passa a ser o pai de x
        conjuntos[x][0] = y
        if(conjuntos[x][1] == conjuntos[y][1]):
            conjuntos[y][1] = conjuntos[y][1] + 1
            
def encontra_conjunto(conjuntos, x):
    noh = x
    pai = conjuntos[noh][0]
    # Iterativamente, busca a raiz da subarvore (quando o id e o pai sao iguais)
    while(noh != pai):
        noh = pai
        pai = conjuntos[noh][0]
    conjuntos[x][0] = pai
    return pai

class Vertice:
    # Construtor default
    def __init__(self, identificador):
        self.__constroi_conjunto(identificador)
        
    '''
    Inicializacao do vertice com seu identificador,
    com o seu pai (que inicialmente eh um ponteiro
    para o proprio vertice) e seu rank (zero)
    '''
    def __constroi_conjunto(self, identificador):
        self.v = identificador
        self.p = identificador
        self.rank = 0

'''
Output: Conjunto de arestas resultantes do Algoritmo de Kruskall.
Armazenaremos em forma de tripla: (u,v,w(u,v)), em que 
u e v são vértices, e w(u,v) é o peso de (u,v) no grafo
testado
'''
def Kruskall(V, w):
    T = [] # Inicializando o conjunto output: nossa AGM.
    
    # Numero de vertices
    n = len(V)
    
    conjuntos = {v: [v, 0] for v in V}

    '''
    Dicionario de arestas ordenadas por peso.
    Complexidade O(mlogm), em que m eh o numero de arestas
    '''
    w_ord = sorted(w.items(), key=lambda x: x[1])

    # Numero de arestas adicionadas
    n_arestas = 0
    
    '''
    Para cada aresta (ja ordenada, pelo peso).
    Complexidade: no pior caso, o loop executa
    O(m)
    '''
    for ((u,v), val) in w_ord:
        conju = encontra_conjunto(conjuntos, u)
        conjv = encontra_conjunto(conjuntos, v)
        if(conju != conjv):
            T.append((u, v, w[(u,v)]))
            n_arestas = n_arestas + 1
            
            # So funciona se o grafo for conexo!
            if(n_arestas == n-1):
                break
            uniao(conju, conjv, conjuntos)
            
    return T

def __main__():
	
	while True:
		# input do 'm' e do 'n'
		m,n = map(int,input().split())

		if m == n ==0:
			
			break

		# Vertices do grafo
		v = []
		# Pesos das arestas do grafo
		w = {}
		
		x = []
		k = 0
		while k < n:
			y = input()
			x.append(y.split())
			
			k += 1
		
		
		i = 0
		while i < n:
			tupla = (int(x[i][0]),int(x[i][1]))
			w[tupla] = int(x[i][2])
			i+=1
		
		v = list(range(m))
		
		# calcula o custo, somatorio dos pesos 
		valorAntigo = 0
		
		for i in w.values():
			valorAntigo += int(i)
		
		# chamada do algoritmo de Kruskall
		AGM = Kruskall(v, w)
		
		# pesos das arestas da AGM
		tree = {}
		
		# Acrescentando suas arestas
		for e in AGM:
			tupla = (e[0],e[1])
			tree[tupla] = (e[2])
		
		# calcula o custo apos o algoritmo de Kruskall
		valorNovo = 0
		
		for i in tree.values():
			valorNovo += int(i)
		
		# calcula a economia que se teve
		economia = valorAntigo - valorNovo
		print(economia)

__main__()
