class Node():

    def __init__(self, parent=None, position=None):
        # Inicialização de um nó com seu pai e posição no labirinto
        self.parent = parent
        self.position = position

        # Custo do ponto inicial até este nó
        self.g = 0  
        # Heurística: estimativa do custo deste nó até o destino
        self.h = 0  
        # Custo total: g + h
        self.f = 0  

    def __eq__(self, other):
        # Verifica se dois nós são iguais com base em suas posições
        return self.position == other.position


def astar(maze, start, end):
    #Retorna uma lista de tuplas como um caminho do ponto inicial dado até o ponto final no labirinto fornecido

    # Criação dos nós de início e fim
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Inicialização das listas aberta e fechada
    open_list = []
    closed_list = []

    # Adiciona o nó de início
    open_list.append(start_node)

    # Loop até encontrar o destino
    while len(open_list) > 0:

        # Obtém o nó atual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Remove o nó atual da lista aberta e o adiciona à lista fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Encontrou o objetivo
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Retorna o caminho reverso

        # Gera filhos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Quadrados adjacentes

            # Obtém a posição do nó
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Garante que esteja dentro dos limites
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Garante terreno caminhável
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Cria um novo nó
            new_node = Node(current_node, node_position)

            # Adiciona à lista de filhos
            children.append(new_node)

        # Loop através dos filhos
        for child in children:

            # Filho já está na lista fechada
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Calcula os valores f, g e h
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Filho já está na lista aberta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Adiciona o filho à lista aberta
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
