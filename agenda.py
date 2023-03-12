"""Requerimientos:
#definir la estructura: una lista de diccionarios que almacene la informacion de cada contacto.
#definir funciones basicas: buscar en agenda, eliminar de agenda, editar, crear y buscar.
funciones:
     #agregar:pedir al usuario ingresar nombre y numero de telf, si no existe, agregar un usuario nuevo
     #editar: pedir al usuario que ingrese nombre o numero, si existe, poder editar
     #buscar: pedir al usuario que ingrese nombre o numero, si existe mostrar, sino, decir que no existe
     #eliminar: pedir al usuario que ingrese nombre y numero, si existe preguntar si esta seguro de eliminar
"""

# Crear una lista de diccionarios que representan los contactos de la agenda
diary = [
    {"nombre": "Andres Perez", "numero": "12345678"},
    {"nombre": "Maria Bonilla", "numero": "87654321"},
    {"nombre": "Jose Peña", "numero": "45678901"},
    {"nombre": "Genesis Santaella", "numero": "77232547"},
    {"nombre": "Miguel Andres", "numero": "6546216"}
]

# Función para buscar un contacto en la agenda
def search_contact(diary):
    # Pedir al usuario el nombre o número del contacto que desea buscar
    search_name = input("Ingrese el nombre o numero del contacto que desea buscar: ")
    # Convertir el texto ingresado por el usuario en título para coincidir con los valores de la agenda
    search = search_name.title()
    # Recorrer cada contacto de la agenda
    for contacto in diary:
        # Si el valor ingresado por el usuario coincide con alguno de los valores de la agenda
        if search in contacto.values():
            # Imprimir el nombre y el número del contacto encontrado
            print("Nombre: {}  Numero: {}".format(contacto["nombre"], contacto["numero"]))
            return
    # Si el contacto no se encuentra en la agenda
    print("El contacto no se encuentra en la agenda")

# Función para agregar un contacto a la agenda
def add_contact(diary):
    # Pedir al usuario el nombre del nuevo contacto
    name_contac = input("Ingrese el nombre del nuevo contacto: ")
    # Convertir el nombre ingresado por el usuario en título
    name = name_contac.title()
    # Pedir al usuario el número del nuevo contacto
    number = input("Ingrese el numero del nuevo contacto: ")
    # Recorrer todos los contactos en la agenda para verificar si el nombre ya existe
    for contact in diary:
        if name == contact["nombre"] or number == contact["numero"]:
            print("El contacto ya existe en la agenda")
            return
    # Crear un diccionario que representa el nuevo contacto
    contact = {"nombre": name, "numero": number}
    # Agregar el nuevo contacto a la agenda
    diary.append(contact)
    # Imprimir un mensaje de éxito
    print("El contacto ha sido agregado a la agenda")

# Función para editar un contacto de la agenda
def edit_contact(diary):
    # Pedir al usuario el nombre o número del contacto que desea editar
    search_name = input("Ingrese el nombre o numero del contacto que desea editar: ")
    # Convertir el texto ingresado por el usuario en título
    search = search_name.title()
    # Recorrer cada contacto de la agenda
    for contact in diary:
        # Si el valor ingresado por el usuario coincide con alguno de los valores de la agenda
        if search in contact.values():
            # Pedir al usuario el nuevo nombre del contacto
            new_name = input("Ingrese el nuevo nombre del contacto: ")
            # Convertir el nuevo nombre en título
            new_name_contact = new_name.title
            # Pedir al usuario el nuevo número del contacto
            new_number = input("Ingrese el nuevo numero del contacto: ")
            # Actualizar el nombre y número del contacto encontrado
            contact["nombre"] = new_name_contact
            contact["numero"] = new_number
            # Imprimir un mensaje de éxito
            print("El contacto ha sido editado correctamente")
            return
    # Si el contacto no se encuentra en la agenda
    print("El contacto no se encuentra en la agenda")

#funcion para eliminar contactos de su lista
def delete_contact(diary):
    #se solicita al usuario que ingrese el nombre a eliminar
    search_name = input("Ingrese el nombre o numero del contacto que desea eliminar: ")
    #se transforma el nombre ingresado en mayusculas cada inicial
    name = search_name.title()
    for contact in diary:
        if name in contact.values():
            diary.remove(contact)
            print("El contacto ha sido eliminado de la agenda")
            return
    print("El contacto no se encuentra en la agenda")

while True:
    print("\n=== AGENDA TELEFÓNICA ===")
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    option = input("Ingrese una opcion: ")

    if option == "1":
        search_contact(diary)
    elif option == "2":
        add_contact(diary)
    elif option == "3":
        edit_contact(diary)
    elif option == "4":
        delete_contact(diary)
    elif option == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida. Intente de nuevo.")
