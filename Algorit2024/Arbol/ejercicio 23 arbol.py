#ejercicio 23 arbol
from arbol_avl import BinaryTree

criaturas = [
    {
        "Criatura": "Ceto",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Tifón",
        "Derrotado por": "Zeus",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Equidna",
        "Derrotado por": "Argos Panoptes",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Pefredo",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Enio",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Escila",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Caribdis",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Euríale",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Esteno",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Medusa",
        "Derrotado por": "Perseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Ladón",
        "Derrotado por": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Águila del Cáucaso",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Quimera",
        "Derrotado por": "Belerofonte",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Hidra de Lerna",
        "Derrotado por": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "León de Nemea",
        "Derrotado por": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Esfinge",
        "Derrotado por": "Edipo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Dragón de la Cólquida",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Cerbero",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Cerda de Cromión",
        "Derrotado por": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Ortro",
        "Derrotado por": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Toro de Creta",
        "Derrotado por": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Jabalí de Calidón",
        "Derrotado por": "Atalanta",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Carcinos",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Gerión",
        "Derrotado por": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Cloto",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Láquesis",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Átropos",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Minotauro de Creta",
        "Derrotado por": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Harpías",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Argos Panoptes",
        "Derrotado por": "Hermes",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Aves del Estínfalo",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Talos",
        "Derrotado por": "Medea",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Sirenas",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Pitón",
        "Derrotado por": "Apolo",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Cierva de Cerinea",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Basilisco",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Jabalí de Erimanto",
        "Derrotado por": None,
        "Descripcion": None,
        "Capturada": None
    }
]

def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')

tree = BinaryTree()

for criatura in criaturas:
    tree.insert_node(criatura['Criatura'], criatura)


# A-listado inorden de las criaturas y quienes la derrotaron
separar()
print("Criatura inorden con la informacion de quien lo derroto:")
tree.inordenCriaturas()

separar()
# B- se debe permitir cargar una breve descripción sobre cada criatura
pos= tree.search("Minotauro de Creta")
if pos is not None:
  pos.other_value["Descripcion"]= "Era una bestia poderosa"
print(pos.other_value)

separar()
# C- mostrar toda la información de la criatura Talos
print("Buscar la informacion de la criatura Talos: ")
pos= tree.search("Talos")
if pos is not None:
  print(pos.other_value)


separar()
# D- determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas

separar()
# E- listar las criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles: ")
tree.inordenCriaturasHeracles()

separar()
# F- listar las criaturas que no han sido derrotadas
print("criaturas que no fueron derrotadas: ")
tree.inordenCriaturasSinDerrota()

separar()
# G- además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo
pos= tree.search("Cierva de Cerinea")
if (pos is not None) and (pos.other_value["Derrotado por"] is None):
  pos.other_value["Capturada"]= input("ingrese heroe que lo capturo: ")
print(pos.other_value)

separar()
# H- modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
pos= tree.search("Cerbero")
if pos is not None:
  pos.other_value["Capturada"]= "Heracles"
print(pos.other_value)
print()
pos= tree.search("Toro de Creta")
if pos is not None:
  pos.other_value["Capturada"]= "Heracles"
print(pos.other_value)
print()
pos= tree.search("Cierva de Cerinea")
if pos is not None:
  pos.other_value["Capturada"]= "Heracles"
print(pos.other_value)
print()
pos= tree.search("Jabalí de Erimanto")
if pos is not None:
  pos.other_value["Capturada"]= "Heracles"
print(pos.other_value)
separar()
# I- se debe permitir búsquedas por coincidencia
buscar=input("ingresar nombre a buscar: ")
tree.proximity_search(buscar)

separar()
# J- eliminar al Basilisco y a las Sirenas
print("eliminar Basilisco")
value_to_delete = 'Basilisco'
delete_value, extra_info = tree.delete_node(value_to_delete)
print("eliminar Sirenas")
value_to_delete = 'Sirenas'
delete_value, extra_info = tree.delete_node(value_to_delete)
print("lista ordenada para corroborar cambios")
tree.inorden()

separar()
# K- modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias
pos= tree.search("Aves del Estínfalo")
if pos is not None:
  pos.other_value["Descripcion"]= "Heracles derroto a varias"
print(pos.other_value)


separar()
# L- modifique el nombre de la criatura Ladón por Dragón Ladón
value_to_delete = 'Ladón'
delete_value, extra_info = tree.delete_node(value_to_delete)
print("buscado:", delete_value)
print("modificacion: Dragón Ladón")
tree.insert_node('Dragón Ladón', extra_info)
tree.proximity_search("Dragón")
separar()
# M- realizar un listado por nivel del árbol
tree.by_level()
separar()

