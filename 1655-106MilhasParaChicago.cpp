/*
Por: Felipe de Oliveira Fernandes e Jonathas Luis de Sousa
GCC218 - Algoritmos em Grafos
Turma: 10A - 2021/01
Universidade Federal de Lavras - UFLA
*/

/*
1655 - 106 Miles To Chicago
O problema apresenta um grafo ponderado bidirecional, que os 
vertices sã o número de interseções, as arestas são o número de
ruas a serem consideradas e os pesos são a probabilidade dos 
irmãos Blue conseguirem usar essa rua sem serem pegos.
Devemos achar o caminho mais seguro, que é considerado a rota
que maximiza a probabilidade deles não serem pegos.

Solução: utilizando uma versão adaptada do algoritmo de Dijkstra,
em vez de encontrar o menor caminho encontrar o maior, e em vez de
somar distancia o peso, multiplicar. Essa mudança foi trivial, ao 
relaxar
          em vez de                fizemos
    if v.d > (u.d + peso):  ->  if v.d < (u.d * peso)
        v.d = u.d + peso            v.d = u.d * peso

Em vez de infinito, a distancia inicial passou a ser -1, e 
e a valor da distancia do veertice origem passou a ser 1.
*/

#include <iostream>
#include <iomanip>
#include <list>
#include <queue>
#define INF -1

using namespace std;

class Vertice
{
    public:
        int v;
        list<pair<int,double>> listaAdj;
        bool visitado;
        double dist;
        
        Vertice(int v)
        {
            this->v = v;
            this->visitado = false;
            this->dist = INF;
        }
        
        Vertice(){}
        
        void AdicionarAresta(int v2,double peso)
        {
            this->listaAdj.push_back(make_pair(v2,peso));
        }     
};

bool operator< (const Vertice& v1, const Vertice &v2)
{
    return v1.dist < v2.dist;
}
        
bool operator> (const Vertice& v1, const Vertice &v2)
{
    return v1.dist > v2.dist;
}

void dijkstra(Vertice v[])
{
    priority_queue<Vertice, vector<Vertice>,greater<vector<Vertice>::value_type> > lp;
    lp.push(v[0]);

    while(!lp.empty())
    {
        Vertice atual = lp.top();
        lp.pop();
            
        if(!atual.visitado)
        {
            atual.visitado = true;
                
            list<pair<int, double> >::iterator it;
        
            for(it = atual.listaAdj.begin(); it != atual.listaAdj.end(); it++)
            {
                int vAdj = it->first;
                double peso = it->second;
                    
                if(v[vAdj].dist < atual.dist * peso)
                {
                    v[vAdj].dist = atual.dist * peso;
                    lp.push(v[vAdj]);
                }
            }
            
        }
    }
}

int main()
{
    int m, n, v1, v2;
    double c;

    while (1)
    {
        cin >> n;

        if (n == 0)
        {
            return 0;
        }

        cin >> m;

        Vertice vertices[n];
        
        for(int i = 0; i < n; i++)
        {
            vertices[i] = Vertice(i);
        }
        
        for(int i = 0; i < m; i++)
        {
            cin>>v1>>v2>>c;
            v1--;
            v2--;
            vertices[v1].AdicionarAresta(v2,c / 100);
            vertices[v2].AdicionarAresta(v1,c / 100);
        }

        vertices[0].dist = 1;

        
        dijkstra(vertices);
        
        double dist = vertices[n - 1].dist;
        
        cout << fixed << setprecision(6);
        cout << dist*100 << " percent" << endl;
    }
}