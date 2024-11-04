#ejercicio 15 nombres grafo
# nombres modernas 
#Chichén Itzá, en Yucatán, México.
#El Coliseo de Roma, en Italia.
#La estatua del Cristo Redentor, en Río de Janeiro, Brasil.
#La Gran Muralla China, en China.
#Machu Picchu, en el Cuzco, Perú
#Petra, en Jordania.
#El Taj Mahal, en Agra, India.

# nombres naturales
# 1) Cataratas del Iguazú (Argentina/Brasil), 
# 2) Isla de Jeju (Corea del Sur), 
# 3) Río Subterráneo Puerto Princesa (Filipinas), 
# 4) Isla de Komodo (Indonesia), 
# 5) Montaña de la Mesa (Sudáfrica), 
# 6) Bahía Ha Long (Vietnam), 
# 7) Amazonia (Bolivia, Brasil, Colombia, Ecuador, Guayana Francesa, Guyana, Perú, Surinam y Venezuela)

from grafo2 import Graph
from random import randint
from lista import show_list_list, by_name, search

def separar():
    print('-------------------------------------------------------')

maravillas = [
    {"nombre":"Chichén Itzá", "pais ubicacion":"México", "tipo" : "arquitectónica"},
    {"nombre":"El Coliseo de Roma", "pais ubicacion":"Italia", "tipo" : "arquitectónica"},
    {"nombre":"La estatua del Cristo Redentor", "pais ubicacion":"Brasil", "tipo" : "arquitectónica"},
    {"nombre":"La Gran Muralla China", "pais ubicacion":"China", "tipo" : "arquitectónica"},
    {"nombre":"Machu Picchu", "pais ubicacion":"Perú", "tipo" : "arquitectónica"},
    {"nombre":"Petra", "pais ubicacion":"Jordania", "tipo" : "arquitectónica"},
    {"nombre":"Taj Mahal", "pais ubicacion":"India", "tipo" : "arquitectónica"},
    #aca empiezan las naturales
    {"nombre":"Cataratas del Iguazú", "pais ubicacion":"Argentina/Brasil", "tipo" : "Natural"},
    {"nombre":"Isla de Jeju", "pais ubicacion":"Corea del Sur", "tipo" : "Natural"},
    {"nombre":"Río Subterráneo Puerto Princesa", "pais ubicacion":"Filipinas", "tipo" : "Natural"},
    {"nombre":"Isla de Komodo", "pais ubicacion":"Indonesia", "tipo" : "Natural"},
    {"nombre":"Montaña de la Mesa", "pais ubicacion":"Sudáfrica", "tipo" : "Natural"},
    {"nombre":"Bahía Ha Long", "pais ubicacion":"Vietnam", "tipo" : "Natural"},
    {"nombre":"Amazonia", "pais ubicacion":"Bolivia/Brasil/Colombia/Ecuador/Guayana Francesa/Guyana/Perú/Surinam/Venezuela", "tipo" : "Natural"},
]

conexiones = [
    {"origen":"Chichén Itzá", "destino":"El Coliseo de Roma", "peso" : randint(100,10000)},{"origen":"Chichén Itzá", "destino":"La estatua del Cristo Redentor", "peso" : randint(100,10000)},{"origen":"Chichén Itzá", "destino":"La Gran Muralla China", "peso" : randint(100,10000)},{"origen":"Chichén Itzá", "destino":"Machu Picchu", "peso" : randint(100,10000)},{"origen":"Chichén Itzá", "destino":"Petra", "peso" : randint(100,10000)},{"origen":"Chichén Itzá", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"El Coliseo de Roma", "destino":"La estatua del Cristo Redentor", "peso" : randint(100,10000)},{"origen":"El Coliseo de Roma", "destino":"La Gran Muralla China", "peso" : randint(100,10000)},{"origen":"El Coliseo de Roma", "destino":"Machu Picchu", "peso" : randint(100,10000)},{"origen":"El Coliseo de Roma", "destino":"Petra", "peso" : randint(100,10000)},{"origen":"El Coliseo de Roma", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"La estatua del Cristo Redentor", "destino":"La Gran Muralla China", "peso" : randint(100,10000)},{"origen":"La estatua del Cristo Redentor", "destino":"Machu Picchu", "peso" : randint(100,10000)},{"origen":"La estatua del Cristo Redentor", "destino":"Petra", "peso" : randint(100,10000)},{"origen":"La estatua del Cristo Redentor", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"La Gran Muralla China", "destino":"Machu Picchu", "peso" : randint(100,10000)},{"origen":"La Gran Muralla China", "destino":"Petra", "peso" : randint(100,10000)},{"origen":"La Gran Muralla China", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"Machu Picchu", "destino":"Petra", "peso" : randint(100,10000)},{"origen":"Machu Picchu", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"Petra", "destino":"Taj Mahal", "peso" : randint(100,10000)},
    {"origen":"Cataratas del Iguazú", "destino":"Isla de Jeju", "peso" : randint(100,10000)},{"origen":"Cataratas del Iguazú", "destino":"Río Subterráneo Puerto Princesa", "peso" : randint(100,10000)},{"origen":"Cataratas del Iguazú", "destino":"Isla de Komodo", "peso" : randint(100,10000)},{"origen":"Cataratas del Iguazú", "destino":"Montaña de la Mesa", "peso" : randint(100,10000)},{"origen":"Cataratas del Iguazú", "destino":"Bahía Ha Long", "peso" : randint(100,10000)},{"origen":"Cataratas del Iguazú", "destino":"Amazonia", "peso" : randint(100,10000)},
    {"origen":"Isla de Jeju", "destino":"Río Subterráneo Puerto Princesa", "peso" : randint(100,10000)},{"origen":"Isla de Jeju", "destino":"Isla de Komodo", "peso" : randint(100,10000)},{"origen":"Isla de Jeju", "destino":"Montaña de la Mesa", "peso" : randint(100,10000)},{"origen":"Isla de Jeju", "destino":"Bahía Ha Long", "peso" : randint(100,10000)},{"origen":"Isla de Jeju", "destino":"Amazonia", "peso" : randint(100,10000)},
    {"origen":"Río Subterráneo Puerto Princesa", "destino":"Isla de Komodo", "peso" : randint(100,10000)},{"origen":"Río Subterráneo Puerto Princesa", "destino":"Montaña de la Mesa", "peso" : randint(100,10000)},{"origen":"Río Subterráneo Puerto Princesa", "destino":"Bahía Ha Long", "peso" : randint(100,10000)},{"origen":"Río Subterráneo Puerto Princesa", "destino":"Amazonia", "peso" : randint(100,10000)},
    {"origen":"Isla de Komodo", "destino":"Montaña de la Mesa", "peso" : randint(100,10000)},{"origen":"Isla de Komodo", "destino":"Bahía Ha Long", "peso" : randint(100,10000)},{"origen":"Isla de Komodo", "destino":"Amazonia", "peso" : randint(100,10000)},
    {"origen":"Montaña de la Mesa", "destino":"Bahía Ha Long", "peso" : randint(100,10000)},{"origen":"Montaña de la Mesa", "destino":"Amazonia", "peso" : randint(100,10000)},
    {"origen":"Bahía Ha Long", "destino":"Amazonia", "peso" : randint(100,10000)},
]

paises= ['México', 'Italia', 'Brasil', 'China', 'Perú', 'Jordania', 'India', 'Argentina', 'Corea del Sur', 'Filipinas', 'Indonesia', 'Sudáfrica', 'Vietnam', 'Bolivia','Colombia','Ecuador','Guayana', 'Francesa','Guyana','Surinam','Venezuela']

#a- cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa
grafo = Graph(dirigido=False)
grafoM = Graph(dirigido=False)
grafoN = Graph(dirigido=False)

print("cargo vertices: ")
for maravilla in maravillas:
    nodo = {
        'value': maravilla["nombre"],
        'other_value':maravilla["pais ubicacion"]+ maravilla["tipo"],
        'aristas': [],
        }
    
    if "arquitectónica" == maravilla["tipo"]:
        grafoM.insert_vertice(maravilla["nombre"],maravilla)
    else:
        grafoN.insert_vertice(maravilla["nombre"],maravilla)
    grafo.insert_vertice(maravilla["nombre"],maravilla)

grafo.show_graph()
separar()
separar()

#b- cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenarla distancia que las separa
print("cargo aristas: ")

for conexion in conexiones:
    nodo_origen = grafo.search222(conexion["origen"])
    if "arquitectónica" == nodo_origen["tipo"]:
        grafoM.insert_arista(conexion["origen"], conexion["destino"], conexion["peso"])
    else:
        grafoN.insert_arista(conexion["origen"], conexion["destino"], conexion["peso"])
    
    grafo.insert_arista(conexion["origen"], conexion["destino"], conexion["peso"])

grafo.show_graph()

separar()
separar()

#c- hallar el árbol de expansión mínimo de cada tipo de las maravillas;
print("Arbol de expansión mínimo para las maravillas arquitectónicas:")
print()
grafo.mark_as_not_visited()
arbolM = grafoM.kruskal("La estatua del Cristo Redentor") 
con=0
for arista in arbolM[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} / peso: {peso}")
    
separar()
separar()

print("Arbol de expansión mínimo para las maravillas naturales:")
print()
grafo.mark_as_not_visited()
arbolN = grafoN.kruskal("Montaña de la Mesa") 
con=0
for arista in arbolN[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"origen: {origen} -> destino: {destino} / peso: {peso}")
    
separar()
separar()


#d- determinar si existen países que dispongan de maravillas arquitectónicas y naturales
print("Los paises que disponen de disponen de maravillas arquitectónicas y naturales son: ")
for pais in paises:
    grafo.buscomaravillas(pais)

separar()
separar()
#e- determinar si algún país tiene más de una maravilla del mismo tipo
print("Los paises que disponen de disponen de más de una maravilla del mismo tipo son: ")
for pais in paises:
    grafo.buscomaravillas222(pais)

separar()
separar()

