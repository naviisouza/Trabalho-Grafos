class Graph:

    def __init__(self, vertices):
        # Inicialização da classe Graph com o número de vértices
        self.V = vertices
        self.graph = []  # Lista para armazenar as arestas do grafo

    def addEdge(self, u, v, w):
        # Método para adicionar uma aresta ao grafo com peso
        self.graph.append([u, v, w])

    def printArr(self, dist):
        # Método para imprimir as distâncias dos vértices a partir da fonte
        print("Vértice \tDistância a partir da Fonte")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        # Implementação do algoritmo de Bellman-Ford para encontrar o caminho mais curto

        # Inicialização das distâncias com infinito, exceto a fonte com distância 0
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Relaxamento das arestas por V - 1 iterações
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Verificação de ciclos de peso negativo
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Grafo contém ciclo de peso negativo")
                return

        # Impressão das distâncias finais
        self.printArr(dist)


if __name__ == '__main__':
    # Criar um objeto da classe Graph
    g = Graph(5)

    # Adicionar arestas ao grafo
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # Executar o algoritmo de Bellman-Ford com a fonte no vértice 0
    g.BellmanFord(0)
