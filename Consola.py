#------------------------ MENU Y OPCION ---------------------------------
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

def validar_sigla(consolas, ventas, sigla):

    if  len(sigla) < 2 or len(sigla) > 5:
        return False
    
    if not (sigla.isalpha() and sigla.isupper()):
        return False
    
    if sigla in consolas or sigla in ventas:
        return False
    
    return True

def validar_nombre(nombre):

    if nombre.strip() == "":
        return False
    
    if len(nombre) < 3 or len(nombre) > 40:
        return False
    
    return True

def validar_fabricante(fabricante):

    if fabricante.strip() == "":
        return False
    
    if len(fabricante) < 2 or len(fabricante) > 30:
        return False
    
    return True

def validar_año(año):

    try:
        año = int(año)

        if año < 1972 or año > 2025:
            return False 
    except:
        return False
        
    return True

def validar_precio(precio):

    try:
        precio = float(precio)

        if precio <= 0:
            return False
    except:
        return False
    
    return True

def validar_stock(stock):

    try:
        stock = int(stock)

        if stock < 0:
            return False
    except:
        return False
    
    return True

#----------------------------- VALIDACIONES CON RETORNO TRUE O FALSE -----------------

def agregar_consola(consolas, ventas):

    while True:

        sigla = input("Ingrese sigla de la consola: ")

        if validar_sigla(consolas, ventas, sigla):
            break
        else:
            print("ERROR: Sigla incorrecta, Min(2-5 caracteres, solo contener mayusculas, no estas repetida)")

    while True:

        nombre = input("Ingrese nombre de la consola: ")

        if validar_nombre(nombre):
            break
        else:
            print("ERROR: Min(3-40 Caracteres y no quedar vacio)")

    while True:

        fabricante = input("Ingrese fabricante: ")

        if validar_fabricante(fabricante):
            break
        else:
            print("ERROR: Min(2-30 Caracteres y no quedar vacio)")

    while True:

        try:
            año = int(input("Ingrese año de lanzamiento: "))

            if validar_año(año):
                break
            else:
                print("ERROR: El año debe ser enter 1972 y 2025")
        except ValueError:
            print("ERROR: No debe contener letras")

    while True:

        try:
            precio = float(input("Ingrese el precio: "))

            if validar_precio(precio):
                break
            else:
                print("ERROR: Precio debe ser mayor a 0")
        except ValueError:
            print("ERROR: No debe contener letras")

    while True:

        try:
            stock = int(input("Ingrese stock: "))

            if validar_stock(stock):
                break
            else:
                print("ERROR: Debe ser mayor o igual a 0")
        except ValueError:
            print("ERROR: No debe contener letras")

    consolas[sigla] = [nombre, fabricante, año]
    ventas[sigla] = [precio, stock]


    



consolas = {}
ventas = {}

while True:

    menu()
    opcionMenu = opcion_menu()

    match opcionMenu:

        case 1:
            agregar_consola(consolas, ventas)




