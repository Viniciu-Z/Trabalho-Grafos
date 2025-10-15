from grafo import Grafo
from acharSubgrafoMinimo import subgrafoMinimo
from analisarGrafo import verificarConexao, retirarAresta
from acharSubgrafoAvancado import encontrarSubgrafoConexo

grafo = Grafo()

grafo.adicionarConexoes('A','B',3)
grafo.adicionarConexoes('A','C',1)
grafo.adicionarConexoes('B','C',4)
grafo.adicionarConexoes('B','D',6)
grafo.adicionarConexoes('C','D',5)
grafo.adicionarConexoes('C','E',2)
grafo.adicionarConexoes('D','E',7)
grafo.adicionarConexoes('D','F',8)
grafo.adicionarConexoes('E','G',3)
grafo.adicionarConexoes('F','G',4)

def questao1(g):
    subrede = subgrafoMinimo(g, 'A')
    return subrede

def questao2(g):
    if verificarConexao(g):
        print("grafo é conexo")
    else:
        print("grafo é desconexo")

    g.mostrarGrafo()
    vertice1 = str(input("Digite o vertice 1: ")).upper()
    vertice2 = str(input("Digite o vertice 2: ")).upper()

    if vertice1 in g.vertices and vertice2 in g.vertices:
        print(f"arestas {vertice1} - {vertice2} retirada")
        if retirarAresta(g, vertice1, vertice2) is True:
            print("grafo continua conexo")
        else:
            print("grafo ficou desconexo")

def questao3(g):
    subrede = encontrarSubgrafoConexo(g)

    print("Arestas do melhor subgrafo:")
    for v, conexoes in subrede.vertices.items():
        print(f"{v}: {conexoes}")


#subgrafo = questao1(grafo)
#questao2(subgrafo)
#questao3(grafo)

'''
*   GRAFO DO SLIDE
grafo.adicionarConexoes('A','B',1100)
grafo.adicionarConexoes('A','C',1800)
grafo.adicionarConexoes('A','D',2000)
grafo.adicionarConexoes('A','F',1200)
grafo.adicionarConexoes('B','C',900)
grafo.adicionarConexoes('B','D',800)
grafo.adicionarConexoes('B','E',750)
grafo.adicionarConexoes('C','D',700)
grafo.adicionarConexoes('C','F',850)
grafo.adicionarConexoes('D','E',1000)
grafo.adicionarConexoes('E','F',500)

* EXEMPLO 2 DO PROFESSOR
grafo.adicionarConexoes('A','B',4)
grafo.adicionarConexoes('A','C',2)
grafo.adicionarConexoes('B','D',5)
grafo.adicionarConexoes('B','E',10)
grafo.adicionarConexoes('C','E',3)
grafo.adicionarConexoes('C','F',8)
grafo.adicionarConexoes('D','G',6)
grafo.adicionarConexoes('E','H',7)
grafo.adicionarConexoes('F','I',1)
grafo.adicionarConexoes('G','J',9)
grafo.adicionarConexoes('H','J',4)
grafo.adicionarConexoes('I','J',2)
'''