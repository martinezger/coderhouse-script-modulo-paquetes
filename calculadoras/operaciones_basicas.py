from math import sqrt

class CalculadoraBasica:

    def __init__(self):
        self.resultado = None

    def suma(self, a, b):
        self.resultado = a + b

    def resta(self, a, b):
        self.resultado = a - b
    
    def multiplicacion(self, a, b):
        self.resultado = a * b
    
    def division(self, a, b):
        self.resultado = a / b

    def print_resultado(self):
        print (self.resultado)
