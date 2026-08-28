class nodo:
    def __init__(self, dato): 
     # entre el def y los dos guiones bajos va un espacio   
        self.dato = dato 
        self.siguiente = None

n1 = nodo(42)
n2 = nodo(78)
n3 = nodo(106)

n1.siguiente = n2
n2.siguiente = n3

actual = n1
cont = 1

while actual is not None:
    print(f"Nodo: {cont} dato {actual.dato} Direccion de memoria: {id(actual)}")
    actual = actual.siguiente
    cont += 1

    def insertar_inicio(self, dato):
        nuevo = nodo(dato)
        nuevo.siguiente = self.head
        self.head = nuevo
        self.size += 1 

class linked_list:
    def __init__(self, head, tail, size):
        self.head = head
        self.tail = tail 
        self.size = size 
        self.dato = dato
def insert_first(self, dato):
    nuevo = nodo(dato) #creo un objeto/instanciar 
    nuevo.siguiente = self.head
    self.head = nuevo
    self.size += 1
