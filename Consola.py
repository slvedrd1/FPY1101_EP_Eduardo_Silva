def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")

def opcion_menu():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except:
            print("ERROR: Debe ingresar una opcion valida (1-5)")




consolas = {}
ventas = {}

while True:

    menu()
    opcionMenu = opcion_menu()



