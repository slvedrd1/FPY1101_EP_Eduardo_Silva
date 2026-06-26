#------------------------ MENU Y OPCION ---------------------------------
def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("==============================")

def opcion_menu():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except ValueError:
            print("ERROR: Debe ingresar una opcion valida (1-5)")

def validar_sigla(consolas, ventas, sigla):

    if  len(sigla) < 2 or len(sigla) > 5:
        return False
    
    if not (sigla.isalnum() and sigla.isupper()):
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

    if año < 1972 or año > 2025:
        return False 
    else:
        return True
    
def validar_precio(precio):
        
    if precio <= 0:
        return False
    else: 
        return True
    
def validar_stock(stock):

    if stock < 0:
        return False
    else:
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

        nombre = input("Ingrese nombre de la consola: ").title()

        if validar_nombre(nombre):
            break
        else:
            print("ERROR: Min(3-40 Caracteres y no quedar vacio)")

    while True:

        fabricante = input("Ingrese fabricante: ").title()

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
    print("--- CONSOLA AGREGADA EXITOSAMENTE ---")
    print("")

def buscar_consola(consola, ventas, sigla):

    if sigla in consola:
        return consola[sigla], ventas[sigla]
    
    return None

def mostrar_consola(consola, ventas):

    if (len(consola) == 0) or (len(ventas) == 0):
        print("--- NO SE ENCUENTRAS CONSOLAS REGISTRADAS ---")
        return
    
    contadorConsolas = 0
    stockAcumulado = 0

    for sigla in consola:

        datosConsola = consola[sigla]
        datosVentas = ventas[sigla]
        contadorConsolas += 1
        stockAcumulado += datosVentas[1]

        print(f"Sigla: {sigla} / Nombre: {datosConsola[0]} / Fabricante: {datosConsola[1]} / Año: {datosConsola[2]} / Precio: {datosVentas[0]} / Stock: {datosVentas[1]}")
    print("==============================")
    print(f"Total consolas: {contadorConsolas}")


consolas = {}
ventas = {}

while True:

    menu()
    opcionMenu = opcion_menu()

    match opcionMenu:

        case 1:
            agregar_consola(consolas, ventas)

        case 2:
            buscar = input("Ingrese la sigla de la consola que desea buscar: ")
            producto = buscar_consola(consolas, ventas, buscar)

            if producto is not None:

                datosC, datosV = producto

                print("=== Consola Encontrada ===   ")
                print(f"Sigla: {buscar}")
                print(f"Nombre: {datosC[0]}")
                print(f"Fabricante: {datosC[1]}")
                print(f"Año lanz.: {datosC[2]}")
                print(f"Precio: ${datosV[0]}")
                print(f"Stock: {datosV[1]} Unidades")
                print("")

            else:
                print("---- PRODUCTO NO ENCONTRADO ----")

        case 3:
            eliminar = input("Ingrese la sigla de la consola que desea eliminar: ")
            producto = buscar_consola(consolas, ventas, eliminar)

            if producto is not None:

                consolas.pop(eliminar)
                ventas.pop(eliminar)
                print(f"--- Consola {eliminar} eliminada correctamente ---")
                print("")

            else:
                print("--- CONSOLA NO ENCONTRADA PARA ELIMINAR ---")

        case 4:
            print("==============================")
            print("LISTADO COMPLETO DE CONSOLAS")
            print("==============================")
            mostrar_consola(consolas, ventas)

        case 5:
            print("-- Saliendo... ---")
            break
        case _:
            print("ERROR: Debe ingresar una opcion valida (1-5)")





