import funcao as func


def menu(G, direcao):

    print("\n========== MENU PRINCIPAL ==========")
    print("(1). Criar arestas")
    print("(2). Remover arestas")
    print("(3). Rotular arestas")
    print("(4). Checar adjacência entre vértices")
    print("(5). Checar adjacência entre arestas")
    print("(6). Checar existência de arestas")
    print("(7). Checar quantidade de vértices e arestas")
    print("(8). Checar se o grafo é vazio ou completo")
    print("(9). Checar vizinhça de um vértice")
    print("(10). Imprimir matriz de adjacência")
    print("(11). Imprimir lista de adjacência")
    print("(12). Gerar arquivo")
    print("Digite QUALQUER OUTRA OPÇÃO para encerrar o programa")

    num = int(input("\nDigite um número referente ao menu acima: "))

    if num == 1:
        func.criarArestas(G, direcao)
    elif num == 2:
        func.removerArestas(G, direcao)
    elif num == 3:
        func.rotularArestas(G, direcao)
    elif num == 4:
        func.adjacenciaVertices(G, direcao)
    elif num == 5:
        func.adjacenciaArestas(G, direcao)
    elif num == 6:
        func.existenciaArestas(G, direcao)
    elif num == 7:
        func.quantidades(G, direcao)
    elif num == 8:
        func.vazioOuCompleto(G, direcao)
    elif num == 9:
        func.vizinhancaVertice(G, direcao)
    elif num == 10:
        func.matrizAdjacencia(G, direcao)
    elif num == 11:
        func.listaAdjacencia(G, direcao)
    elif num == 12:
        func.gerarArquivo(G, direcao)
    else:
        exit()
