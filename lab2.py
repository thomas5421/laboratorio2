class DNode:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def estaVacia(self):
        return self.head is None

    def agregarAlFinal(self, valor):
        nuevo = DNode(valor)
        if self.estaVacia():
            self.head = nuevo
            self.tail = nuevo
            return

        nuevo.prev = self.tail
        self.tail.next = nuevo
        self.tail = nuevo

    def agregarAlInicio(self, valor):
        nuevo = DNode(valor)
        if self.estaVacia():
            self.head = nuevo
            self.tail = nuevo
            return

        nuevo.next = self.head
        self.head.prev = nuevo
        self.head = nuevo

    def insertarEnPosicion(self, valor, posicion):
        if posicion <= 0:
            self.agregarAlInicio(valor)
            return

        nuevo = DNode(valor)
        actual = self.head
        indice = 0

        while actual is not None and indice < posicion:
            actual = actual.next
            indice += 1

        if actual is None:
            self.agregarAlFinal(valor)
            return

        nuevo.prev = actual.prev
        nuevo.next = actual

        if actual.prev is not None:
            actual.prev.next = nuevo
        else:
            self.head = nuevo

        actual.prev = nuevo

    def eliminarAlInicio(self):
        if self.estaVacia():
            print("La lista doblemente enlazada está vacía.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def eliminarAlFinal(self):
        if self.estaVacia():
            print("La lista doblemente enlazada está vacía.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def buscar(self, valor):
        actual = self.head
        posicion = 0
        while actual is not None:
            if actual.valor == valor:
                return posicion
            actual = actual.next
            posicion += 1
        return -1

    def mostrarAdelante(self):
        actual = self.head
        print("HEAD -> ", end="")
        while actual is not None:
            print(actual.valor, end=" <-> ")
            actual = actual.next
        print("NULL")

    def mostrarAtras(self):
        actual = self.tail
        print("TAIL -> ", end="")
        while actual is not None:
            print(actual.valor, end=" <-> ")
            actual = actual.prev
        print("NULL")

    def cantidadElementos(self):
        actual = self.head
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador

    def mayorElemento(self):
        if self.estaVacia():
            print("La lista doblemente enlazada está vacía.")
            return None

        actual = self.head
        mayor = actual.valor
        while actual is not None:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.next
        return mayor

    def menorElemento(self):
        if self.estaVacia():
            print("La lista doblemente enlazada está vacía.")
            return None

        actual = self.head
        menor = actual.valor
        while actual is not None:
            if actual.valor < menor:
                menor = actual.valor
            actual = actual.next
        return menor

    def promedio(self):
        if self.estaVacia():
            print("La lista doblemente enlazada está vacía.")
            return None

        actual = self.head
        suma = 0
        contador = 0
        while actual is not None:
            suma += actual.valor
            contador += 1
            actual = actual.next
        return suma / contador


if __name__ == "__main__":
# Crear la lista doblemente enlazada
    lista = DoublyLinkedList()
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                # Evitar líneas vacías
                if linea != "":
                    valor = int(linea)
                    # Insertar el valor en la lista
                    lista.agregarAlInicio(valor)
                    lista.mostrarAdelante()
                    print(f"Cantidad de elementos: {lista.cantidadElementos()}")

        with open("Reporte.txt", "w") as archivo:
            archivo.write("====================================\n")
            archivo.write("    REPORTE DE TEMPERATURAS\n")
            archivo.write("====================================\n\n")
            archivo.write(
                "Cantidad de temperaturas: "
                + str(lista.cantidadElementos())
                + "\n"
            )
            archivo.write(
                "Temperatura mayor: "
                + str(lista.mayorElemento())
                + "\n"
            )
            archivo.write(
                "Temperatura menor: "
                + str(lista.menorElemento())
                + "\n"
            )
            archivo.write(
                "Promedio de temperaturas: "
                + str(lista.promedio())
                + "\n"
            )
            archivo.write(
                "Promedio de temperaturas: thomas calvelo"
                + "\n"
            )



    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()

    except ValueError:
        print("Error: el archivo contiene un dato que no es entero.")
        exit()


