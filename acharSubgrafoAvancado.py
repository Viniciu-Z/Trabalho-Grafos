#   QUESTÃO_3

from analisarGrafo import verificarConexao
from grafo import Grafo

def gerarSubgrafo(arestas):
    subgrafos = []

    def gerarSubgrafoRecursao(i, atual):
        if i == len(arestas):
            if atual:
                subgrafos.append(atual[:])
            return

        gerarSubgrafoRecursao(i + 1, atual)
        atual.append(arestas[i])
        gerarSubgrafoRecursao(i + 1, atual)
        atual.pop()

    gerarSubgrafoRecursao(0, [])
    return subgrafos

def verificarCritico(grafo):
    for vertice in grafo.vertices:
        for vizinho in list(grafo.vertices[vertice]):
            if vertice < vizinho:
                peso = grafo.vertices[vertice][vizinho]

                grafo.vertices[vertice].pop(vizinho)
                grafo.vertices[vizinho].pop(vertice)

                conexo = verificarConexao(grafo)

                grafo.vertices[vertice][vizinho] = peso
                grafo.vertices[vizinho][vertice] = peso

                if not conexo:
                    return False
    return True

def encontrarSubgrafoConexo(grafo):
    arestas = []
    visitados = set()
    menorCusto = None
    menorSubgrafo = None

    for vertice, conexoes in grafo.vertices.items():
        for vizinho, peso in conexoes.items():
            arestaOrdenada = tuple(sorted((vertice, vizinho)))
            if arestaOrdenada not in visitados:
                arestas.append((arestaOrdenada[0], arestaOrdenada[1], peso))
                visitados.add(arestaOrdenada)

    subgrafos = gerarSubgrafo(arestas)

    for sub in subgrafos:
        subgrafo = Grafo()
        for v in grafo.vertices:
            subgrafo.vertices[v] = {}

        custo = 0
        for v1, v2, peso in sub:
            subgrafo.vertices[v1][v2] = peso
            subgrafo.vertices[v2][v1] = peso
            custo += peso

        if not verificarConexao(subgrafo):
            continue
        if not verificarCritico(subgrafo):
            continue

        if menorCusto is None or custo < menorCusto:
            menorCusto = custo
            menorSubgrafo = subgrafo
    print(f"custo total: {menorCusto}")
    return menorSubgrafo
