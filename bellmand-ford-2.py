class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printSolution(self, dist):
        print("Menor distância entre todos os pares:")
        for i in range(self.V):
            for j in range(self.V):
                print(dist[i][j], end="\t")
            print()

    def bellmanFord2(self):
        # Inicializa a matriz de distâncias com infinito
        dist = [[float('inf') for _ in range(self.V)] for _ in range(self.V)]

        # Inicializa a distância de um vértice para ele mesmo como 0
        for i in range(self.V):
            dist[i][i] = 0

        # Relaxa todas as arestas repetidamente para encontrar a menor distância
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u][v] > dist[u][u] + w + dist[v][v]:
                    dist[u][v] = dist[u][u] + w + dist[v][v]

        # Imprime a solução
        self.printSolution(dist)
