from Operacao import Operacao
from OperacaoFabrica import OperacaoFabrica


class Calculadora:
    def __init__(self,valor1, valor2, operador):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operador = operador
        
   
    def realizaCalculo (self):
        valor = self.operador.calcula(self.valor1,self.valor2)
        # so lembrando que operador ja vem instanciado como soma, subtracao ou divisao
        # por isso usamos heranca em Operacao.calcula > Soma,subtracao ou divisao
        return valor