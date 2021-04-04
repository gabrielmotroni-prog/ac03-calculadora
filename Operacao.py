from abc import ABCMeta, abstractmethod

class Operacao(metaclass=ABCMeta):
	@abstractmethod
	def calcula(self, n1, n2):   
		pass
	
	

