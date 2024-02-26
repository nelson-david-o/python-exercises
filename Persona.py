class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('Llamando metodo get nombre')
        return self._nombre

    @property
    def apellido(self):
        print('Llamando metodo get apaellido')
        return self._apellido

    @property
    def edad(self):
        print('Metodo get edad')
        return self._edad

    @nombre.setter
    def update(self, nombre):
        print('Llamando metodo set nombre')
        self._nombre = nombre

    @apeliido.setter
    def updateApellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def updateEdad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Nelson','Ortiz',25)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
persona1.update = 'Tony'
persona1.updateApellido = 'stark'
persona1.updateEdad = 26
persona1.mostrar_detalle()