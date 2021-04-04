# aqui eh o conceito factory/ fabrica que eh o instaciador

#padrao stragy-estategia eh: vamos quebrar as responsabilidades e separando cada 'imposto'
#em uma classe especifica 

#utilizamos esses padroes para resolver problemas recorrentes
# como nesse caso criamos varias classes ao inves de varias comparacoes 

from  Operacao import  Operacao
from Soma import  Soma
from Subtracao import  Subtracao
from Divisao import  Divisao
from Multiplicacao import  Multiplicacao


class OperacaoFabrica():
    def __init__(self, operador:str):
        self.operador = operador
        print(self.operador)

    
    def criar(self) -> Operacao: #Especificamente, o '->' marca a anotação da função de retorno.
        if self.operador == 'soma':
            return Soma()
        elif self.operador == 'subtracao':
            return Subtracao()
        elif self.operador == 'multiplicacao':
            return Multiplicacao()
        else:
            return Divisao()