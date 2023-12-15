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


if __name__ == "__main__":
    # Criar um objeto da classe Graph
    g = Graph(9)
    # Definir a matriz de adjacência do grafo
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    # Executar o algoritmo de Dijkstra com a fonte no vértice 0
    g.dijkstra(0)
