class AreaRectangulo:

    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def formula(self):
        return self.base * self.altura

base = int(input(f'Proporcione la base: '))
altura = int(input(f'Proporcione la altura: '))
rectangulo = AreaRectangulo(base, altura)

print(f"Área del rectangulo es: {rectangulo.formula()}")