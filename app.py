import os
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
from math import sqrt
from Soma import Soma
from Subtracao import Subtracao
from Divisao import Divisao
from Operacao import Operacao
from Calculadora import Calculadora
from OperacaoFabrica import OperacaoFabrica

app = Flask(__name__)

@app.route('/calc/<int:valor1>/<int:valor2>/<operacao>',  methods=['GET',])
def calculadoraweb(valor1,valor2,operacao):
 
    operacao = str(operacao)

    try: # validando o tipo das variavel
        v1 = int(valor1)
    except ValueError:
        abort(404)
    
    try: # validando o tipo das variavel
        v2 = int(valor2)
    except ValueError:
        abort(404)

    try: # validando divisao por 0
        valor1/valor2
    except Exception as ZeroDivisionError:
        abort(404)
  
  

    #if v2 == 0 and operacao == 'divisao': # validao para nao dividir por 0 chuleira
    #    abort(404)
    
  

    operacao_returno = OperacaoFabrica(operacao).criar()#instancia a Operacao com base no parametro da url
    #operacao_returno = OperacaoFabrica("subtracao").criar()
    print(operacao_returno,"eh a operacao")
    calculadora_retorno = Calculadora(v1,v2, operacao_returno).realizaCalculo() # passo os valores e a operacao ja instanciada
    #calculadora_retorno = Calculadora(v1,v2, Subtracao()).realizaCalculo()
    print(calculadora_retorno)
    
    return str(calculadora_retorno)


@app.errorhandler(404)
def page_not_found(error):
    print("erro de operacao")
    return render_template('error.html'), 404

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #print('Opa digitado ' + name)
    
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)

