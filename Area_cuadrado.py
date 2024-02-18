class AreaCuadrado:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def hallarAreaCuadrado(self):
        return self.lado1 * self.lado2

ResultadoArea = int(input(f'Proporcione el lado 1 del cuadrado: '))
ResultadoArea2 = int(input(f'Proporcione el lado 2 del cuadrado: '))

cuadrado = AreaCuadrado(ResultadoArea, ResultadoArea2)
print(f'Área del cuadrado es: {cuadrado.hallarAreaCuadrado()}')
