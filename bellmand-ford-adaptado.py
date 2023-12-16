class Graph:

    def __init__(self, vertices):
        # Inicializa um grafo com o número especificado de vértices
        self.V = vertices
        # Cria uma matriz para representar as arestas entre vértices
        # Inicialmente, todas as distâncias são definidas como infinito
        self.graph = [[float("inf")] * self.V for _ in range(self.V)]
        # Inicializa a diagonal principal da matriz com zeros, pois a menor distância de um vértice para ele mesmo é zero
        for i in range(self.V):
            self.graph[i][i] = 0

    def addEdge(self, u, v, w):
        # Adiciona uma aresta ao grafo com peso w entre os vértices u e v
        self.graph[u][v] = w

    def printSolution(self, dist):
        # Imprime a matriz de distâncias entre todos os pares de vértices
        print("Menor distância entre todos os pares:")
        for i in range(self.V):
            for j in range(self.V):
                # Se a distância é infinita, imprime "INF"
                if dist[i][j] == float("inf"):
                    print("INF", end="\t")
                # Caso contrário, imprime a distância
                else:
                    print(dist[i][j], end="\t")
            print()

    def floydWarshall(self):
        # Cria uma cópia da matriz de distâncias para realizar os cálculos
        dist = [row[:] for row in self.graph]

        # Atualiza a matriz de distâncias considerando todos os vértices como intermediários
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    # Atualiza a distância se encontrar um caminho mais curto passando por k
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Imprime a solução
        self.printSolution(dist)