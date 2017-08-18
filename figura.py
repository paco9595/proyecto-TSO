from enum import Enum
class figura(Enum):
    def __init__(self,alto,ancho,tipo):
         self.alto = alto
         self.ancho = ancho
         self.tipo = tipo
    def girarPiezas(objetos):
        array = []
        for objeto in objetos:
            if (objeto.ancho > objeto.alto):
                aux= objeto.ancho 
                objeto.ancho=objeto.alto
                objeto.alto = aux
            array.push(objeto)
        return array

objetos ={
    'rectangulos': [],
    'circulos':[],
    'rectangulos':[],
    'irregulares':[]
    } 
for x in range(5):
    print x
    aux =   (10+x,10-x)
    objetos.rectangulos.push(aux)
print objetos.rectangulos