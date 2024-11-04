#ejercicio 14 pagina 234 PDF
# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from grafo import Graph
from random import randint,choice

def separar():
    print('-------------------------------------------------------')

Ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1','baño 2','habitacion 1','habitacion 2','sala de estar','terraza','patio']

conexiones = [
    {"origen":"cocina", "destino":"comedor", "peso" : randint(0,10)},{"origen":"cocina", "destino":"sala de estar", "peso" : randint(0,10)}, {"origen":"cocina", "destino":"terraza", "peso" : randint(0,10)},{"origen":"cocina", "destino":"baño 1", "peso" : randint(0,10)},{"origen":"cocina", "destino":"baño 2", "peso" : randint(0,10)},
    {"origen":"comedor", "destino":"terraza", "peso" : randint(0,10)},{"origen":"comedor", "destino":"sala de estar", "peso" : randint(0,10)},{"origen":"comedor", "destino":"habitacion 2", "peso" : randint(0,10)},{"origen":"comedor", "destino":"habitacion 1", "peso" : randint(0,10)},
    {"origen":"cochera", "destino":"baño 2", "peso" : randint(0,10)},{"origen":"cochera", "destino":"quincho", "peso" : randint(0,10)},{"origen":"cochera", "destino":"habitacion 1", "peso" : randint(0,10)},
    {"origen":"quincho", "destino":"baño 2", "peso" : randint(0,10)},{"origen":"quincho", "destino":"patio", "peso" : randint(0,10)},
    {"origen":"baño 1", "destino":"habitacion 1", "peso" : randint(0,10)},{"origen":"baño 1", "destino":"terraza", "peso" : randint(0,10)},{"origen":"baño 1", "destino":"sala de estar", "peso" : randint(0,10)},
    {"origen":"patio", "destino":"habitacion 2", "peso" : randint(0,10)},{"origen":"patio", "destino":"sala de estar", "peso" : randint(0,10)},
    {"origen":"habitacion 2", "destino":"baño 2", "peso" : randint(0,10)},
]


#cargar ambientes punto a
grafo = Graph(dirigido=False)
for ambiente in Ambientes:
    nodo = {
        'value': ambiente,
        'aristas': [],
        }
    grafo.insert_vertice(ambiente)

grafo.show_graph()

separar()

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

for conexion in conexiones:
    grafo.insert_arista(conexion["origen"], conexion["destino"], conexion["peso"])

grafo.show_graph()

separar()

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
grafo.mark_as_not_visited()
print ("soy el kruskal: ")
arbol = grafo.kruskal("cocina")
con=0
for arista in arbol[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} / peso: {peso}")
    elpeso= int(peso)
    con = con + elpeso

separar()
print("la cantidad de metros de cable necesario para conectar dos ambientes son: ",con)
separar()

grafo.mark_as_not_visited()


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para 
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

camino= grafo.dijkstra("habitacion 1")
destino = "sala de estar"
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0] )
        destino = value[1][2]
camino_completo.reverse()
print(f'el camino mas corto es: {'-'.join(camino_completo)} con un costo de {peso_total}')

separar ()
