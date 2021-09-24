/* Por: Felipe de Oliveira Fernandes e Jonathas Luis de Sousa
GCC218 - Algoritmos em Grafos
Turma: 10A
Universidade Federal de Lavras - UFLA 

2323 - Móbile
Como resolver: esse problema apresenta um grafo direcionado, onde as peças são os vértices e as linhas que
sustentam as peças são as arestas, de forma que a aresta (u,v) indica a ligação entre as peças i e j.
O objetivo é verificar se um móbile está balanceado, se para cada peça, todos os sub-móbiles pendurados nela
são compostos pelo mesmo número de peças, ou seja, peças irmãs devem possuir o mesmo número de descendentes.
Para a solução aplicamos um algoritmo de Lista de Adjacência para verificar esse balanceamento. Para isso,
armazenamos o grau de cada vértice, pois apenas vértices com grau maior do que 1 podem estar mal balanceados.
Além disso, armazenamos a quantidade de descendentes cada vértice possui, para realizar comparações, por meio
de uma função recursiva.
Assim, dado um vértice com grau maior que 1 verifica-se a quantidade de descendentes tem seus filhos.
*/

// [START program]
// [START imports]
#include <iostream>
#include <vector>
using namespace std;
// [END imports]

// Função recursiva para determinar quantos filhos tem uma peça.
// Soma a quantidade de filhos (size) recursivamente até chegar a um Nó folha
int tam(vector<int>*lista_adj, int v){
    int valor = lista_adj[v].size();

    for(int v1 : lista_adj[v]){
        valor += tam(lista_adj,v1);
    }
    return valor;
}

int main(){

    // Número de peças utilizadas no móbile
    int n;
    cin >> n;

    // Lista de Adjacência
    vector<int>* lista_adj = new vector<int>[n+1];

    // Grau dos vértices
    int* grau = new int[n+1];

    // Inicialização do grau do nó i
    for(int i = 1; i <= n; i++){
        grau[i] = 0;
    }

    // Leitura das arestas
    for(int x=0;x<n;x++){
        int u,v;
        cin >> v >> u;

        lista_adj[u].push_back(v); //v -> u

        grau[u]++;
    }

    // Vetor para armazenar os Tamanhos dos sub-móbiles (descendentes)
    int tamanhos[n+1];
    for(int x=1;x<=n;x++){
        // Armazena a quantidade de filhos
        int qtd = lista_adj[x].size();

        // Percorre os filhos
        for(int v : lista_adj[x]){
            qtd += tam(lista_adj,v);
        }
        tamanhos[x] = qtd;
    }

    // Verificação do balanceamento
    bool resultado = true;
    
    // Percorre o lista
    // Para os vértices que tem grau maior do que 1, faz-se a comparação
    for(int x=1;x<n+1;x++){ 
        if(grau[x] > 1){ 
            // Pega-se o primeiro elemento como referência e compara com os outros
            int comparador = tamanhos[lista_adj[x].front()];
            for(int v : lista_adj[x]){
                // se o número de filhos for diferente está desbalanceado
                // Força a parada do loop que percorre os itens da lista
                if(comparador != tamanhos[v]){
                    resultado = false;
                    break;
                }
            }
        }
        // Se o número de filhos for diferente, também força a parada do loop que percorre toda a lista
        if (resultado == false){
            break;
        }
    }

    if(resultado){
        cout << "bem" << endl;
    }else
        cout << "mal" << endl;
}
// [END program]
