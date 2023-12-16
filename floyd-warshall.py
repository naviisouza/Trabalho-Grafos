# Número de vértices no grafo
V = 4

# Valor infinito usado para representar a distância entre vértices não conectados
INF = 99999


def floydWarshall(graph):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],
                                dist[i][k] + dist[k][j])

    printSolution(dist)


def printSolution(dist):
    print("A seguinte matriz mostra as distâncias mais curtas entre cada par de vértices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()

    floydWarshall(graph)
