# Funções

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")



#exibir_mensagem()
#exibir_mensagem_2(nome="Luan")
#exibir_mensagem_3()
#exibir_mensagem_3(nome="Luan Vieira Teixeira")

# Retornando valores

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])
print(calcular_total([10, 20, 34]))
#64

retorna_antecessor_e_sucessor(10)
print(retorna_antecessor_e_sucessor(10))
#(9, 11)

# Argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    # Salva carro no banco de dados..
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", "1999", "ABC-1234")
salvar_carro(marca="Fiat",modelo="Palio",ano="1999",placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo":"Palio", "ano":"1999","placa":"ABC-1234"})

# Args e kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quinta, 03 de Abril de 2025","Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

# Parâmetros especiais

#Sintaxe
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#    -------------    ----------     ----------
#           |              |               |
#   |Positional only|      |        |Keyword only|
#                |Positional or Keyword|
#Exemplos:

#Positional Only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido

#Keyword Only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Válido

#Keyword and positional only

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Válido


# Objetos de primeira classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicação)
#Eu passei uma função para referência para dentro de outra função

op = somar

print(op(1, 23))
#Atribui a função para outra variavel.


#Escopo local e escopo global

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500) # 2500
print(salario) # 2500