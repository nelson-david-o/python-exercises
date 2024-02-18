class Persona:

# *args para argumentos variables como tupla
# **args para argumentos variables de tipo diccionario
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')

persona1 = Persona('Nelson','Ortiz',25, '311600790', 2,3,5, m='manzana', p='pera')
persona1.mostrar_detalle()


persona2 = Persona('Elsa','Fernandez',27)
persona2.mostrar_detalle()