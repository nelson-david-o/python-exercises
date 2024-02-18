class Cubo:
    def __init__(self, ancho,alto,profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundida = profundidad

    def hallarVolumen(self):
        return self.ancho * self.alto * self.profundida

v_ancho = int(input(f'Proporcione el ancho del cubo: '))
v_alto = int(input(f'Proporcione el alto del cubo: '))
v_profundidad = int(input(f'Proporcione la profundidad: '))

resultadoVolumen = Cubo(v_ancho,v_alto,v_profundidad)
print(f'Volumen de un cubo es: {resultadoVolumen.hallarVolumen()}')