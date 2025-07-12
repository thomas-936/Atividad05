class estudiante:
    def __init__(self, nombre, carnet, carrera, nota_final):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota_final = nota_final

        def mostar_info():
            print(f"Nombre: {self.nombre}")
            print(f"Carnet: {self.carnet}")
            print(f"Carrera: {self.carrera}")
            print(f"Nota final: {self.nota_final}")

lista_estudiantes = []

def resgistrar_estudiante():
    print("Registrar nuevo estudiante: ")
    nombre = input("Nombre: ")
    carnet = input("Carnet: ")
    carrera = input("Carrera: ")
    nota_final = float(input("Ingrese la nota final: "))
    estudiantes1 = estudiante(nombre, carnet, carrera, nota_final)
    lista_estudiantes.append(estudiantes1)
    print("Estudiante ingresado correctamente...")


def mostrar_estidiantes():
    print("Los estudiantes registrados son: ")
    if len(lista_estudiantes)== 0:
        print("\nNo hay estudiantes registrados... ")
    else:
        for estu in lista_estudiantes:
            print(f"-{estu}")

def buscar():
    buscar_carnet = input("Ingrese el carnet ha buscar")
    encontrado = 0
    for i in lista_estudiantes:
        if i.carnet == buscar_carnet:
            print("Estudiante encontarado...")
            encontrado=1
            break

    if encontrado ==0:
        print("El estudiante no ha sido encontrado.")

def calcular_promedio():
    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        suma_total = 0
        for j in lista_estudiantes:
            suma_total+=j.nota_final
        promedio = suma_total/ len(lista_estudiantes)
        print(f"El promedio de notas de los estudiantes es: {promedio} ")
