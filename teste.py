
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor #Para criar uma instância, é obrigatório preencher os valores de todos os atributos.#

def extrato(conta):
    print("saldo {}".format(conta["saldo"])) #O paradigma Orientado a Objetos nos incentiva a agrupar funcionalidades relacionadas em um mesmo lugar. Este é um dos principais problemas.#



