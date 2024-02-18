class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Nelson','Ortiz',25)
#persona1.mostrar_detalle()
Persona.mostrar_detalle(persona1)
persona1.telefono = 978856478
print(persona1.nombre, persona1.apellido, persona1.edad, persona1.telefono)


persona2 = Persona('Elsa','Fernandez',27)
persona2.mostrar_detalle()