#   QUESTÃO_1

from grafo import Grafo

def subgrafoMinimo(grafo, inicio):
    print("Construindo subgrafo...")
    visitados = {inicio}
    subgrafo = Grafo()
    custoTotal = 0

    while len(visitados) < len(grafo.vertices):
        menorPeso = None
        menorVizinho = None
        verticeInicial = None

        for vertice in visitados:
            for vizinho, peso in grafo.vertices[vertice].items():
                if vizinho not in visitados:
                    if menorPeso is None or peso < menorPeso:
                        menorPeso = peso
                        menorVizinho = vizinho
                        verticeInicial = vertice
        visitados.add(menorVizinho)
        subgrafo.adicionarConexoes(verticeInicial, menorVizinho, menorPeso)
        custoTotal += menorPeso

        print(f"aresta adicionada: {verticeInicial} - {menorVizinho} - {menorPeso}")
    print(f"custo total: {custoTotal}")
    return subgrafo
