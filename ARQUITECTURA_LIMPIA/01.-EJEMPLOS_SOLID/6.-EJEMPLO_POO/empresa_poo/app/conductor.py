class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo = None

    def asignar_vehiculo(self, vehiculo): # moto, auto, camion, auto_electrico
        self.vehiculo = vehiculo
        print(f"{self.nombre} ahora está conduciendo un {vehiculo.marca} {vehiculo.modelo}.")

    def conducir(self):
        if self.vehiculo:
            print(self.vehiculo.conducir())
        else:
            print(f"{self.nombre} no tiene un vehículo asignado.")

    def cargar_combustible(self, litros):
        if self.vehiculo:
            print(self.vehiculo.cargar_combustible(litros))
        else:
            print(f"{self.nombre} no tiene un vehículo asignado para cargar combustible.")