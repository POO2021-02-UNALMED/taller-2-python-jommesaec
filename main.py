class Asiento():
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        colores = ['rojo','verde','amarillo','negro','blanco']
        if color in colores:
            self.color = color

class Auto():
    cantidadCreados = 0
    AsientosCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):        
        for i in self.asientos:
            if i != None: 
                self.AsientosCreados +=1
        return self.AsientosCreados
        
    def verificarIntegridad(self):
        reg = []
        for i in self.asientos:
            if i != None:                
                reg.append(i.registro)
        
        for i in reg:
            print(i)
            if self.registro == self.motor.registro == i:
                return "Auto original"
            else:
                return "Las piezas no son originales"

class Motor():
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo == "electrico"  or tipo == "gasolina":
            self.tipo = tipo