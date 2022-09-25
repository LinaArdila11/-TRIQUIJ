class Tablero:


    def __init__ (self):

        # Definir nuestra matriz de 3x3
        self.matriz=[
            ["","",""],
            ["","",""],
            ["","",""]
        ]
    def verificarJugada (self,X,Y):
        
        if  self.matriz[X][Y]=="":
            return False
        else:
            return True