#CONSIGNAS DEL TP
from grafo import Grafo
from grafo import Cola
from grafo import Pila

def bfs_diccionario_padres(grafo, origen, destino):
    visitados = set()
    padres = {}
    q = Cola()
    visitados.append(origen)
    padres[origen] = None
    orden[origen] = None
    q.encolar(origen)
    while !q.esta_vacia():
        v = q.desencolar
        if v == destino:
            break
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.agregar(w)
                padre[w] = v
                orden[w] = orden[w] + 1
                q.encolar(w)
    return padres.values, orden

def camino(grafo, pag1, pag2):
    recorrido, costo = bfs_diccionario_padres(grafo, origen, destino)
    recorrido.split("->")
    print(recorrido)
    print("Costo:",costo)

def navegacion(grafo,origen):
    v = grafo.adyacentes(origen)[0]
    recorrido = []
    recorrido.append(v)
    i = 0
    while i < 20 and v != None:
        v = grafo.adyacentes(origen)[0]
    recorrido.split("->")
