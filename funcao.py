import time

import networkx as nx

import menu as m


def voltar(G, direcao):

    input("\nPressione ENTER para retornar ao menu.")

    m.menu(G, direcao)


def criarGrafo(numVertices, direcao):
    if direcao == 1:
        G = nx.Graph()
        for x in range(1, numVertices + 1):
            G.add_node(input("\nDigite o rótulo do vétice " + str(x) + ": "),
                       weight=float(input("Digite o peso do vértice " + str(x) + ": ")))

    elif direcao == 2:
        G = nx.DiGraph()
        for x in range(1, numVertices + 1):
            G.add_node(input("\nDigite o rótulo do vétice " + str(x) + ": "),
                       weight=float(input("Digite o peso do vértice " + str(x) + ": ")))
    return G


def lerArquivo(caminho):
    G = nx.read_gml(caminho)
    return G


def criarArestas(G, direcao):
    v1 = input("\nDigite o rótulo do primeiro vértice da aresta: ")
    v2 = input("Digite o rótulo do segundo vértice da aresta: ")
    peso = float(input("Digite o peso da aresta: "))

    G.add_edge(v1, v2, weight=peso)

    valor = int(
        input("\nDigite 1 para criar uma nova aresta ou 2 para retornar ao menu: "))

    if valor == 1:
        criarArestas(G, direcao)

    voltar(G, direcao)


def removerArestas(G, direcao):
    v1 = input("\nDigite o rótulo do primeiro vértice da aresta: ")
    v2 = input("Digite o rótulo do segundo vértice da aresta: ")

    G.remove_edge(v1, v2)

    valor = int(
        input("\nDigite 1 para remover outra aresta ou 2 para retornar ao menu: "))

    if valor == 1:
        removerArestas(G, direcao)

    voltar(G, direcao)


def rotularArestas(G, direcao):
    v1 = input("\nDigite o rótulo do primeiro vértice da aresta: ")
    v2 = input("Digite o rótulo do segundo vértice da aresta: ")
    rotulo = input("Digite um rótulo para a aresta: ")
    aresta = [v1, v2]

    nx.set_edge_attributes(G, aresta, rotulo)

    print("\nO rótulo " + rotulo + " foi adicionado à aresta " + v1 + v2 + ".")

    voltar(G, direcao)


def adjacenciaVertices(G, direcao):
    v = input("\nDigite o rótulo de um dos vértices existentes: ")

    print("\nVértices adjacentes: ")
    print([n for n in G.neighbors(v)])

    voltar(G, direcao)


def adjacenciaArestas(G, direcao):
    v1 = input("\nDigite o rótulo do primeiro vértice da aresta: ")
    v2 = input("Digite o rótulo do segundo vértice da aresta: ")

    arestas = list(G.edges)

    print("\nArestas adjacentes: ")

    for i in range(len(arestas)):
        if arestas[i] == (v1, v2):
            pass

        elif v1 in arestas[i]:
            print(arestas[i])

        elif v2 in arestas[i]:
            print(arestas[i])

        else:
            pass

    voltar(G, direcao)


def existenciaArestas(G, direcao):
    v1 = input("\nDigite o rótulo do primeiro vértice da aresta: ")
    v2 = input("Digite o rótulo do segundo vértice da aresta: ")

    if G.has_edge(v1, v2) is True:
        print("\nExiste.")

    else:
        print("\nNão existe.")

    voltar(G, direcao)


def vazioOuCompleto(G, direcao):
    arestas = G.number_of_edges()
    vertices = G.number_of_nodes()

    if arestas == 0:
        print("\nO grafo é vazio.")

    elif arestas == (vertices * (vertices - 1))/2:
        print("\nO grafo é completo.")

    else:
        print("\nO grafo não é vazio e também não é completo.")

    voltar(G, direcao)


def matrizAdjacencia(G, direcao):
    print("\nMatriz de adjacência: ")

    A = nx.to_scipy_sparse_array(G)

    print(A.todense())

    voltar(G, direcao)


def listaAdjacencia(G, direcao):
    print("\nLista de adjacência: ")

    for line in nx.generate_adjlist(G):
        print(line)

    voltar(G, direcao)


def gerarArquivo(G, direcao):
    nx.write_gml(G, "grafo.gml")
    print("\nO arquivo foi salvo na mesma pasta do código fonte.")
  
    voltar(G, direcao)


def quantidades(G, direcao):
    print("\nNúmero de arestas: ")
    print(G.number_of_edges())

    print("Número de vértices: ")
    print(G.number_of_nodes())

    voltar(G, direcao)

def vizinhancaVertice(G, direcao):
    v = input("\nDigite o rótulo de um dos vértices existentes: ")

    vizinhos = list(G.neighbors(v))

    print("\nVizinhança do vértice " + v + ": ")
    print(vizinhos)

    voltar(G, direcao)
