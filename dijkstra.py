import sys

class Graph():

    def __init__(self, vertices):
        # Inicialização do grafo com o número de vértices
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        # Método para imprimir a solução com as distâncias
        print("Vértice \tDistância a partir da Fonte")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        # Função para encontrar o vértice com a menor distância
        min = sys.maxsize

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        # Implementação do algoritmo de Dijkstra para encontrar o caminho mais curto

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Encontrar o vértice com a menor distância
            x = self.minDistance(dist, sptSet)

            # Marcar o vértice como visitado
            sptSet[x] = True

            # Atualizar as distâncias dos vértices adjacentes
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        # Imprimir a solução final
        self.printSolution(dist)

    # Executar o algoritmo de Dijkstra com a fonte no vértice 0
    g.dijkstra(0)
