from Jugador import Jugador
from Tablero import Tablero
class Juego:


    def __init__ (self):

        self.mijugador=Jugador()
        self.miTablero=Tablero()

    def jugarTriqui(self):

        self.mijugador.miFicha.simbolo= "X"


        self.mijugador.realizar_jugada(self.miTablero)
        self.mijugador.realizar_jugada(self.miTablero)

miJuego=Juego()
miJuego.jugarTriqui()