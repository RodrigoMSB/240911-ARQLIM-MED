from trabajador import Trabajador

class Desarrollador(Trabajador):
    def trabajar(self):
        return "Estoy escribiendo código"
    
    def tomar_descanso(self):
        return "Estoy tomando un descanso"
    
    def reportar(self):
        # Este método no es relevante para Desarrollador, pero debe implementarlo
        return "Esto está vacío, lo siento, es un mal diseño"