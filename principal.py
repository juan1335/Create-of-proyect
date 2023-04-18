import registros

def menu():
    print("MENU DE OPCIONES:")
    print("1- Cargar proyecto")
    print("2- Mostrar proyecto")
    print("3- Actualicar proyecto")
    print("4- Resumen por lenguaje")
    print("5- Resumen por año")
    print("6- Filtrar lenguaje")
    print("7- Productividad")
    print("8- Salir")
    opc = int(input("Ingrese la opción que desee: "))
    return opc

def menu_de_lenguaje():
    print("MENU DE LENGUAJES DISPONIBLES:")
    print("0- Python")
    print("1- Java")
    print("2- C++")
    print("3- Javascript")
    print("4- SHELL")
    print("5- HTML")
    print("6- Ruby")
    print("7- Swift")
    print("8- C#")
    print("9- VB")
    print("10- Go")

def ordenar(vector):
    for i in range(len(vector)-1):
        for j in range(i+1, len(vector)):
            if vector[i].titulo > vector[j].titulo:
                vector[i], vector[j] = vector[j], vector[i]

def ordenar_numero(vector):
    for i in range(len(vector)-1):
        for j in range(i+1, len(vector)):
            if vector[i].numero_proyecto > vector[j].numero_proyecto:
                vector[i], vector[j] = vector[j], vector[i]

def mostrar_proyectos(vector):
    print("Lista de proyectos:")
    print(f'{"Proyecto":<10} {"Titulo":<10} {"Fecha":^10} {"Lenguaje":<10} {"Codigos":>10}')
    print("=" * 74)
    for i in range(len(vector)):
        registros.to_string(vector[i])

def buscar_proyecto(vector, x):
    cod = -1
    for i in range(len(vector)):
        if x == vector[i].numero_proyecto:
            print("~"* 10)
            print("SI EXISTE")
            print("~"* 10)
            print(f'{"Proyecto":<10} {"Titulo":<10} {"Fecha":^10} {"Lenguaje":<10} {"Codigos":>10}')
            registros.to_string(vector[i])
            while cod < 0:
                  cod = int(input("Ingrese el valor nuevo de la cantidad de codigo del programa: "))
                  if cod < 0:
                      print("ERROR ingrese un numero positivo")
            vector[i].cantidad_codigo = cod
            dia, mes, year = registros.modificar_fecha()
            vector[i].fecha_actualizada = str(dia) + "/" + str(mes) + "/" + str(year)
            print("Vector actualizado: ")
            print(f'{"Proyecto":<10} {"Titulo":<10} {"Fecha":^10} {"Lenguaje":<10} {"Codigos":>10}')
            registros.to_string(vector[i])
            print("~"* 26)
            print("ACTUALIZACION EXITOSA")
            print("~"* 26)
            return
    print("~"* 10)
    print("NO EXISTE")
    print("~"* 10)

def codigo_x_lenguaje(contadores, vector):
    for i in range(len(vector)):
        leng = vector[i].lenguaje
        contadores[leng] = contadores[leng] + vector[i].cantidad_codigo

def mostrar_contador(contadores):
    print("La cantidad de lineas de codigo por lenguaje es de:")
    print(f'{"Lenguaje":<10} {"Codigos":<10}')
    print("=" * 18)
    for i in range(len(contadores)):
        print(f'{registros.nombre_lenguaje(i):<10} {contadores[i]:<10}')

def proyectos_x_year(proyecto_year, vector):
    for i in range(len(vector)):
        contador = 0
        first = True
        for j in vector[i].fecha_actualizada:
            contador += 1
            if contador >= 9:
                if first:
                   years = j
                   first = False
                else:
                   years += j
        proyecto_year[int(years)] = proyecto_year[int(years)] + 1

def mostrar_proyecto_year(proyecto_year):
    print("La cantidad de Proyectos por lenguaje es de:")
    print(f'{"Año":<10} {"Proyectos":<10}')
    print("=" * 20)
    for i in range(len(proyecto_year)):
        if proyecto_year[i] != 0:
            print(f'{year_actualizacion(i):<10} {proyecto_year[i]:<10}')

def year_actualizacion(i):
    if i == 0:
        return "2000"
    elif i == 1:
        return "2001"
    elif i == 2:
        return "2002"
    elif i == 3:
        return "2003"
    elif i == 4:
        return "2004"
    elif i == 5:
        return "2005"
    elif i == 6:
        return "2006"
    elif i == 7:
        return "2007"
    elif i == 8:
        return "2008"
    elif i == 9:
        return "2009"
    elif i == 10:
        return "2010"
    elif i == 11:
        return "2011"
    elif i == 12:
        return "2012"
    elif i == 13:
        return "2013"
    elif i == 14:
        return "2014"
    elif i == 15:
        return "2015"
    elif i == 16:
        return "2016"
    elif i == 17:
        return "2017"
    elif i == 18:
        return "2018"
    elif i == 19:
        return "2019"
    elif i == 20:
        return "2020"
    elif i == 21:
        return "2021"
    elif i == 22:
        return "2022"


def proyectos_lenguaje(vector, ln):
    print("Lista de proyectos:")
    print(f'{"Proyecto":<10} {"Titulo":<10} {"Fecha":^10} {"Lenguaje":<10} {"Codigos":>10}')
    print("=" * 74)
    for i in range(len(vector)):
        if vector[i].lenguaje == ln:
            registros.to_string(vector[i])

def mayor_proyectos(proyectos_year):
    mayor = -1
    for i in range(len(proyectos_year)):
        if mayor == -1:
            mayor = proyectos_year[i]
        else:
            if mayor < proyectos_year[i]:
                mayor = proyectos_year[i]
    return mayor

def mostrar_mayor_proyecto(mayor, proyecto_year):
    print("Los años con mayor cantidad de proyectos actualizados son:")
    print(f'{"Año":<10} {"Proyectos":<10}')
    print("=" * 20)
    for i in range(len(proyecto_year)):
        if mayor == proyecto_year[i]:
            print(f'{year_actualizacion(i):<10} {proyecto_year[i]:<10}')

def principal():
    vector = []
    opc = 0
    calculo = False
    while opc != 8:
        opc = menu()
        if opc == 1:
            n = -1
            calculo = False
            while n < 1 or n > 9999:
                  n = int(input("Ingrese la cantidad de proyectos sin excederse del limite de (9999): "))
                  if n < 1 or n > 9999:
                      print("ERROR ingrese un numero positivo mayor a cero y dentro del rango permitido:")
            registros.generar_datos(vector, n)
            print("~" * 36)
            print("SE CARGO EL PROYECTO EXITOSAMENTE")
            print("~" * 36)
        elif len(vector) != 0 and (opc >= 2 and opc <=7):
            if opc == 2:
                ordenar(vector)
                mostrar_proyectos(vector)
            elif opc == 3:
                x = int(input("Ingrese el numero del proyecto que se quiere buscar: "))
                buscar_proyecto(vector, x)
            elif opc == 4:
                contadores = [0] * 11
                codigo_x_lenguaje(contadores, vector)
                mostrar_contador(contadores)
            elif opc == 5:
                proyectos_year = [0] * 23
                proyectos_x_year(proyectos_year, vector)
                mostrar_proyecto_year(proyectos_year)
                calculo = True
            elif opc == 6:
                ln = -1
                while ln<0 or ln>10:
                    menu_de_lenguaje()
                    ln = int(input("Ingrese el numero del lenguaje de los proyectos que quiera buscar: "))
                    if ln<0 or ln>10:
                        print("ERROR ingrese un numero dentro de las opciones")
                ordenar_numero(vector)
                proyectos_lenguaje(vector, ln)
            elif opc == 7:
                if calculo == True:
                    mayor = mayor_proyectos(proyectos_year)
                    mostrar_mayor_proyecto(mayor, proyectos_year)
                else:
                    print("Haga primero el resumen por año (OPC-5)")
        elif opc >= 2 and opc <=7:
            print("Cargue primero el proyecto con la OPC(1-)")
        elif opc == 8:
            print("Gracias por usar el programa")
            print("QUE TENGA BUEN DIA!")
        else:
            print("ERROR elija una opcion dentro del menu")



if __name__ == "__main__":
    principal()
