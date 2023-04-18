import random

dias = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20" , "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

class Proyectos:
    def __init__(self, num_proyect, titulo, fecha_actualizada, lenguaje, cant_codigo):
        self.numero_proyecto = num_proyect
        self.titulo = titulo
        self.fecha_actualizada = fecha_actualizada
        self.lenguaje = lenguaje
        self.cantidad_codigo = cant_codigo

def nombre_lenguaje(pro):
    if pro == 0:
        return "Python"
    elif pro == 1:
        return "Java"
    elif pro == 2:
        return "C++"
    elif pro == 3:
        return "Javascript"
    elif pro == 4:
        return "Shell"
    elif pro == 5:
        return "HTML"
    elif pro == 6:
        return "Ruby"
    elif pro == 7:
        return "Swift"
    elif pro == 8:
        return "C#"
    elif pro == 9:
        return "VB"
    elif pro == 10:
        return "Go"


def to_string(pro):
    lenguaje = nombre_lenguaje(pro.lenguaje)
    print(f'{pro.numero_proyecto:<10} {pro.titulo:<10} {pro.fecha_actualizada:^10} {lenguaje:<10} {pro.cantidad_codigo:>10}')

def generar_datos(vector, n):
    contador = 0
    while contador < n:
        regist = crear_proyecto()
        bus = buscar_por_proyecto(vector, regist)
        if bus == -1:
            vector.append(regist)
            contador += 1

def crear_proyecto():
    titulos = ("The theory", "Lol player", "Scientific", "Xbox", "Play", "ED SHERAN")
    dia = random.choice(dias)
    mes = str(random.choice(meses))
    year = str(random.randint(2000 ,2022))
    num_proyect = random.randint(1000, 9999)
    titulo = random.choice(titulos)
    fecha_actualizada = dia + "/" + mes + "/" + year
    lenguaje = random.randint(0,10)
    cant_codigo = random.randint(10000, 60000)
    return Proyectos(num_proyect, titulo, fecha_actualizada, lenguaje, cant_codigo)

def modificar_fecha():
    x = -1
    y = -1
    z = -1
    dia = mes = year = 0
    while x < 0:
        se_pudo_dia = False
        dia = str(input("Ingrese el dia a cambiar con formato dd entre el (01-31): "))
        for i in dias:
            if dia == i:
                x = 1
                se_pudo_dia = True
        if not se_pudo_dia:
            print("ERROR, asegurese de poner el dia en formato dd")

    while y < 0:
        se_pudo_mes = False
        mes = str(input("Ingrese el mes a cambiar con formato mm entre el (01-12)"))
        for i in meses:
            if mes == i:
                y = 1
                se_pudo_mes = True
        if not se_pudo_mes:
            print("ERROR, asegurese de poner el dia en formato mm")

    while z < 0:
        se_pudo_year = False
        year = int(input("Ingrese el año a cambiar con formato yyyy entre los años (2000-2022):"))
        for i in range(2000, 2023):
            if year == int(i):
                z = 1
                se_pudo_year = True
        if not se_pudo_year:
            print("ERROR, asegurese de poner el dia en formato yyyy")

    return dia, mes, year

def buscar_por_proyecto(vector, regist):
    bus = -1
    for i in range(len(vector)):
        if vector[i].numero_proyecto == regist.numero_proyecto:
            bus = 0
            break
    return bus
