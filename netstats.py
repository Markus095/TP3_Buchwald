#llamadas a funciones crear el grafo con el archivo
from grafo import Grafo
import grafo_red
grafo = Grafo(True)

def crear_grafo(archivo):
    with open(archivo, encoding="utf8") as file:
        for linea in file:
            linea = linea.split("   ")
            v = linea[0]
            grafo.agregar_vertice(linea[0])
        for link in linea[1::]:
            grafo.agregar_arista(v,link)



def ejecutar_comando(grafo, comando):
    comando = comando.split(" ")
    if(comando[0] == "navegacion"):
        navegacion(grafo, comando[1])
    if(comando[0] == "camino"):
        camino(grafo,comando[1],comando[2])
    if()


def main():
    crear_grafo("wiki-reducido-75000.tsv")
    print("se creo el grafo")
    comando = input()
    while comando != None
        ejecutar_comando(grafo, comando)
        comando = input()
    return 0

main()
