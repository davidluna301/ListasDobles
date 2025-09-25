import random

# ------------------ Clase Nodo ------------------
class Node:
    def __init__(self, data):
        self.data = data  # diccionario con nombre, tamaño, permisos
        self.prev = None
        self.next = None


# ------------------ Clase Lista Doble ------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            print("❌ Índice fuera de rango")
            return

        if index == 0:
            self.add_first(data)
            return
        elif index == self.size:
            self.add_last(data)
            return

        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print("❌ Índice fuera de rango")
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
        self.size -= 1

    def display(self):
        temp = self.head
        i = 0
        while temp:
            print(f"[{i}] {temp.data}")
            temp = temp.next
            i += 1


# ------------------ Generación de Datos ------------------
def generar_locales():
    nombres = [f"Local_{i+1}" for i in range(20)]
    tamanos = [random.randint(50, 300) for _ in range(20)]  # en m²
    permisos = [random.choice(["Comercial", "Residencial", "Mixto"]) for _ in range(20)]

    locales = []
    for i in range(20):
        locales.append({
            "nombre": nombres[i],
            "tamaño": tamanos[i],
            "permiso": permisos[i]
        })
    return locales


# ------------------ Menú Interactivo ------------------
def menu():
    dll = DoublyLinkedList()
    locales = generar_locales()

    # Insertar los 20 locales al inicio
    for local in locales:
        dll.add_last(local)

    while True:
        print("\n=== Gestión de Cachés (Lista Doble) ===")
        print("1. Listar locales")
        print("2. Agregar al inicio")
        print("3. Agregar al final")
        print("4. Insertar en posición")
        print("5. Eliminar en posición")
        print("6. Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
            dll.display()
        elif op == "2":
            nombre = input("Nombre del local: ")
            tamaño = int(input("Tamaño en m²: "))
            permiso = input("Permiso (Comercial/Residencial/Mixto): ")
            dll.add_first({"nombre": nombre, "tamaño": tamaño, "permiso": permiso})
        elif op == "3":
            nombre = input("Nombre del local: ")
            tamaño = int(input("Tamaño en m²: "))
            permiso = input("Permiso (Comercial/Residencial/Mixto): ")
            dll.add_last({"nombre": nombre, "tamaño": tamaño, "permiso": permiso})
        elif op == "4":
            index = int(input("Índice donde insertar: "))
            nombre = input("Nombre del local: ")
            tamaño = int(input("Tamaño en kb: "))
            permiso = input("Permiso (Comercial/Residencial/Mixto): ")
            dll.insert_at(index, {"nombre": nombre, "tamaño": tamaño, "permiso": permiso})
        elif op == "5":
            index = int(input("Índice a eliminar: "))
            dll.remove(index)
        elif op == "6":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.")


# ------------------ MAIN ------------------
if __name__ == "__main__":
    menu()
