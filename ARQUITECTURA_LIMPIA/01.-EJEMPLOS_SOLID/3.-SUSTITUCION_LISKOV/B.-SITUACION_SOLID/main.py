from pinguino import Pinguino
from ave_voladora import AveVoladora
from pato import Pato

# Uso
if __name__ == "__main__":
    pinguino = Pinguino()
    golondrina = AveVoladora()
    pato = Pato()
    
    # Uso polimórfico del método moverse
    print(f"Pingüino: {pinguino.moverse()}")
    print(f"Golondrina: {golondrina.moverse()}")
    print(f"Pato: {pato.moverse()}")