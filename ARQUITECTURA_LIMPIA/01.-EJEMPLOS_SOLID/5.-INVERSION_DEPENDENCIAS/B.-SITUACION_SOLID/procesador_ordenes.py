from almacenamiento import Almacenamiento

class ProcesadorOrdenes:
    def __init__(self, almacenamiento: Almacenamiento):
        self.almacenamiento = almacenamiento

    def procesar(self, orden):
        # Lógica de procesamiento
        print(f"Procesando la orden: {orden}")
        self.almacenamiento.guardar_orden(orden)