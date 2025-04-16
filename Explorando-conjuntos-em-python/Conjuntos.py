a = {1, 2 ,3 ,3} 
print(a) # {1, 2, 3}
# Com {} é a criação de um Conjunto/Set

b = [1, 2 ,3 ,3]
print(b) # [1, 2, 3, 3]
# Com [] é a criação de uma Lista

c = (1, 2, 3, 3,)
print(c)
# Com () é a criação de uma Tupla

#Declarando um conjunto

a = {1, 2 ,3 ,3} 
print(a) # {1, 2, 3}
# Com {} é a criação de um Conjunto/Set

# Conjunto
# set não garante a ordem

set([1, 2, 3, 1, 3, 4]) # {1, 2 ,3 ,4}

set ("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}



#Acessando os dados
# Como não conseguimos acessar os valores de um set, temos que transforma-lo em List

numeros = {1, 2, 3, 2} # {1, 2, 3}

numeros = list(numeros)

numeros[0]

#Iterar conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#Função Enumerate

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")