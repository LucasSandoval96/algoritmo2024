# Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes,
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett,
#  C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2,BB-8


from grafo import Graph
from random import randint

def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')

nombres_star_wars = ["Luke Skywalker","Darth Vader","Yoda","Boba Fett","C-3PO","Leia","Rey","Kylo Ren","Chewbacca","Han Solo","R2-D2","BB-8"]

conexiones = [
    {'origen':'Luke Skywalker', 'destino':'Darth Vader', 'peso' : 50},{'origen':'Luke Skywalker', 'destino':'Yoda', 'peso' : 40},{'origen':'Luke Skywalker', 'destino':'Boba Fett', 'peso' : 755},{'origen':'Luke Skywalker', 'destino':'C-3PO', 'peso' : 436},{'origen':'Luke Skywalker', 'destino':'Leia', 'peso' : 90},{'origen':'Luke Skywalker', 'destino':'Rey', 'peso' : 77},{'origen': 'Luke Skywalker', 'destino': 'Kylo Ren', 'peso': 461},{'origen': 'Luke Skywalker', 'destino': 'Chewbacca', 'peso': 429},{'origen': 'Luke Skywalker', 'destino': 'Han Solo', 'peso': 116},{'origen': 'Luke Skywalker', 'destino': 'R2-D2', 'peso': 702},{'origen': 'Luke Skywalker', 'destino': 'BB-8', 'peso': 808},
    {'origen': 'Darth Vader', 'destino': 'Yoda', 'peso': 404},{'origen': 'Darth Vader', 'destino': 'Boba Fett', 'peso': 619},{'origen': 'Darth Vader', 'destino': 'C-3PO', 'peso': 816},{'origen': 'Darth Vader', 'destino': 'Leia', 'peso': 19},{'origen': 'Darth Vader', 'destino': 'Rey', 'peso': 764},{'origen': 'Darth Vader', 'destino': 'Kylo Ren', 'peso': 634},{'origen': 'Darth Vader', 'destino': 'Chewbacca', 'peso': 276},{'origen': 'Darth Vader', 'destino': 'Han Solo', 'peso': 208},{'origen': 'Darth Vader', 'destino': 'R2-D2', 'peso': 204},
    {'origen': 'Yoda', 'destino': 'Boba Fett', 'peso': 874},{'origen': 'Yoda', 'destino': 'C-3PO', 'peso': 356},{'origen': 'Yoda', 'destino': 'Leia', 'peso': 660},{'origen': 'Yoda', 'destino': 'Rey', 'peso': 162},{'origen': 'Yoda', 'destino': 'Kylo Ren', 'peso': 970},{'origen': 'Yoda', 'destino': 'Chewbacca', 'peso': 927},{'origen': 'Yoda', 'destino': 'Han Solo', 'peso': 931},{'origen': 'Yoda', 'destino': 'R2-D2', 'peso': 952},{'origen': 'Yoda', 'destino': 'BB-8', 'peso': 662},
    {'origen': 'Boba Fett', 'destino': 'C-3PO', 'peso': 26},{'origen': 'Boba Fett', 'destino': 'Leia', 'peso': 121},{'origen': 'Boba Fett', 'destino': 'Rey', 'peso': 126},{'origen': 'Boba Fett', 'destino': 'Kylo Ren', 'peso': 825},{'origen': 'Boba Fett', 'destino': 'Chewbacca', 'peso': 615},{'origen': 'Boba Fett', 'destino': 'Han Solo', 'peso': 648},{'origen': 'Boba Fett', 'destino': 'R2-D2', 'peso': 420},{'origen': 'Boba Fett', 'destino': 'BB-8', 'peso': 265},
    {'origen': 'C-3PO', 'destino': 'Leia', 'peso': 993},{'origen': 'C-3PO', 'destino': 'Rey', 'peso': 162},{'origen': 'C-3PO', 'destino': 'Kylo Ren', 'peso': 154},{'origen': 'C-3PO', 'destino': 'Chewbacca', 'peso': 275},{'origen': 'C-3PO', 'destino': 'Han Solo', 'peso': 784},{'origen': 'C-3PO', 'destino': 'R2-D2', 'peso': 969},{'origen': 'C-3PO', 'destino': 'BB-8', 'peso': 344},
    {'origen': 'Leia', 'destino': 'Rey', 'peso': 458},{'origen': 'Leia', 'destino': 'Kylo Ren', 'peso': 361},{'origen': 'Leia', 'destino': 'Chewbacca', 'peso': 358},{'origen': 'Leia', 'destino': 'Han Solo', 'peso': 331},{'origen': 'Leia', 'destino': 'R2-D2', 'peso': 675},{'origen': 'Leia', 'destino': 'BB-8', 'peso': 223},
    {'origen': 'Rey', 'destino': 'Kylo Ren', 'peso': 410},{'origen': 'Rey', 'destino': 'Chewbacca', 'peso': 346},{'origen': 'Rey', 'destino': 'Han Solo', 'peso': 741},{'origen': 'Rey', 'destino': 'R2-D2', 'peso': 525},{'origen': 'Rey', 'destino': 'BB-8', 'peso': 10},
    {'origen': 'Kylo Ren', 'destino': 'Chewbacca', 'peso': 633},{'origen': 'Kylo Ren', 'destino': 'Han Solo', 'peso': 870},{'origen': 'Kylo Ren', 'destino': 'R2-D2', 'peso': 811},{'origen': 'Kylo Ren', 'destino': 'BB-8', 'peso': 382},
    {'origen': 'Chewbacca', 'destino': 'Han Solo', 'peso': 549},{'origen': 'Chewbacca', 'destino': 'R2-D2', 'peso': 329},{'origen': 'Chewbacca', 'destino': 'BB-8', 'peso': 767},
    {'origen': 'Han Solo', 'destino': 'R2-D2', 'peso': 809},{'origen': 'Han Solo', 'destino': 'BB-8', 'peso': 433},
    {'origen': 'R2-D2', 'destino': 'BB-8', 'peso': 11},
]

grafo = Graph(dirigido=False)

# for origen in nombres_star_wars:
#     for destino in nombres_star_wars:
#         if origen != destino:
#             conexiones.append({
#                 "origen": origen,
#                 'destino': destino,
#                 'peso': randint(0, 1000)
#             })


#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan
for nombre in nombres_star_wars:
    nodo = {
        'value': nombre,
        'aristas': [],
        }
    grafo.insert_vertice(nombre)

for conexion in conexiones:
    grafo.insert_arista(conexion['origen'], conexion['destino'], conexion['peso'])

grafo.show_graph()

separar()

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda
grafo.mark_as_not_visited()
print ("soy el kruskal: ")
arbol = grafo.kruskalmodificado("Yoda")
estoy="no"
for arista in arbol[0].split(';'):
    origen, destino, peso = arista.split('/')
    print(f"origen: {origen} -> destino: {destino} / peso: {peso}")
    if origen == "Yoda" or destino == "Yoda":
        estoy="esta yoda"

separar()
if estoy != "no":
    print("yoda esta en el arbol de expansion minimo")

separar()

#c) determinar cuál es el número máximo de episodio que comparten dos personajes
print("La personajes con mas episodios compartidos son: ")
data=grafo.max_episodios_compartidos()
print(data)
