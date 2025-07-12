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
