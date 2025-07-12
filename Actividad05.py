import traceback


class Estudiante:
    def __init__(self, nombre, carnet, carrera, nota_final):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota_final = nota_final

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Carnet: {self.carnet}")
        print(f"Carrera: {self.carrera}")
        print(f"Nota final: {self.nota_final}")


lista_estudiantes = []


def registrar_estudiante():
    print("Registrar nuevo estudiante: ")
    nombre = input("Nombre: ")
    carnet = input("Carnet: ")
    carrera = input("Carrera: ")
    nota_final = float(input("Ingrese la nota final: "))
    estudiantes1 = Estudiante(nombre, carnet, carrera, nota_final)
    lista_estudiantes.append(estudiantes1)
    print("Estudiante ingresado correctamente...")


def mostrar_estudiantes():
    print("\nLos estudiantes registrados son: ")
    if len(lista_estudiantes)== 0:
        print("\nNo hay estudiantes registrados... ")
    else:
        for estu in lista_estudiantes:
            estu.mostrar_info()
            print("---------------------------")

def buscar():
    buscar_carnet = input("Ingrese el carnet a buscar: ")
    encontrado = 0
    for i in lista_estudiantes:
        if i.carnet == buscar_carnet:
            print("Estudiante encontrado...")
            i.mostrar_info()
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
        print(f"\nEl promedio de notas de los estudiantes es: {promedio} ")

def main():
    opcion = 0
    while opcion != 5:
        print("\n ++MENU++")
        print("1. Registrar un nuevo estudiante: ")
        print("2. Mostrar estudiantes. ")
        print("3. Buscar por Carnet. ")
        print("4. Calcular promedio de notas. ")
        print("5. Salir. ")

        try:
            opcion = int(input("Ingrese su opción: "))
        except Exception:
            print("Ocurrio un error al ingresar la opción.")
            traceback.print_exc()
            continue

        match opcion:
            case 1:
                registrar_estudiante()
            case 2:
                mostrar_estudiantes()
            case 3:
                buscar()
            case 4:
                calcular_promedio()
            case 5:
                print("Saliendo del programa... ")
                break
            case _:
                print("Opción no valida")

if __name__== "__main__":
     main()