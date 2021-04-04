import unittest
from Calculadora  import Calculadora
from Soma import Soma
from Subtracao import Subtracao
from Divisao import Divisao
from Multiplicacao import Multiplicacao

#testes unitarios
class MyTestCase(unittest.TestCase):
    def test_soma(self):
        testeSoma = Calculadora(1, 5, Soma()).realizaCalculo()
        self.assertEqual(testeSoma, 6)
    
    def test_subtracao(self):
        testeSubtracao = Calculadora(3, 2, Subtracao()).realizaCalculo()
        self.assertEqual(testeSubtracao, 1)

    def test_divisao(self):
        testeDivisao = Calculadora(4, 2, Divisao()).realizaCalculo()
        self.assertEqual(testeDivisao, 2)
    
    def test_multiplicacao(self):
        testeMultiplicacao = Calculadora(3, 3, Multiplicacao()).realizaCalculo()
        self.assertEqual(testeMultiplicacao, 9)


if __name__ == '__main__':
    unittest.main(verbosity=2) # parametro 'verbosity=2' espeficica cada metodo de teste acima com ok ou fail
