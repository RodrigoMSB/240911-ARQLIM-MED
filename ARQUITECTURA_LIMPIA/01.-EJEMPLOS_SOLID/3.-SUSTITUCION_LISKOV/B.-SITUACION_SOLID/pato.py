from ave import Ave

class Pato(Ave):
    def volar(self):
        return "Estoy volando"
    
    def nadar(self):
        return "Estoy Nadando"

    def moverse(self):
        return self.nadar() + self.volar()