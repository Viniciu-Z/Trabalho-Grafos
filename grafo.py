class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionarConexoes(self, vertice, vizinho, peso):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
        if vizinho not in self.vertices:
            self.vertices[vizinho] = {}

        self.vertices[vertice][vizinho] = peso
        self.vertices[vizinho][vertice] = peso

    def mostrarGrafo(self):
        for vertice, conexoes in self.vertices.items():
            print(f"{vertice}: {conexoes}")
