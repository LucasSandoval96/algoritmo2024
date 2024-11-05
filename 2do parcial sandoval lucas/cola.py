class Queue:

    def __init__(self): #inicializa
        self.__elements = []

    def arrive(self, element):  #agrega al final
        self.__elements.append(element)

    def attention(self):    #eliminar 
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self): #mostrar tamaño
        return len(self.__elements)

    def on_front(self): #te dice el primer elemento 
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self): #mueve al final 
        element = self.attention()
        if element is not None:
            self.arrive(element)