from caluladoras.operaciones_basicas import CalculadoraBasica


class CalculadoraCientifica(CalculadoraBasica):

    def raiz_cuadrada(self, a):
        self.resultado = sqrt(a)

    def potenciacion(self, a , b):
        self.resultado = a**b