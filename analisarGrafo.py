#   QUESTÃO_2

def verificarConexao(grafo):
    verticeInicial = next(iter(grafo.vertices))

    visitados = []
    fila = [verticeInicial]

    while fila:
        vertice = fila.pop()

        if vertice not in visitados:
            visitados.append(vertice)
            for vizinho in grafo.vertices[vertice]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
    if len(visitados) == len(grafo.vertices):
        return True
    else:
        return False

def retirarAresta(grafo, verticeInicial, verticeFinal):

    peso = grafo.vertices[verticeInicial]

    grafo.vertices[verticeInicial].pop(verticeFinal)
    grafo.vertices[verticeFinal].pop(verticeInicial)

    conexo = verificarConexao(grafo)

    grafo.vertices[verticeInicial][verticeFinal] = peso
    grafo.vertices[verticeFinal][verticeInicial] = peso

    if conexo:
        return True
    else:
        return False
