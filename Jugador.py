def __init__ (self):

        self.miFicha=Ficha()

        
def realizar_jugada(self,unTablero):

        X=-1
        Y=-1
        while unTablero.verificarJugada(X,Y)==False:
             while X>2 or X<0:
                 X=int(input("Ingresa la fila"))

        
             while Y>2 or Y<0:
                Y=int(input("Ingresa la columna"))
        
             unTablero.matriz[X][Y]= self.miFicha.simbolo

        return unTablero