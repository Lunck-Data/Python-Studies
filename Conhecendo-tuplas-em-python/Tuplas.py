# Criando Tuplas
# Se não declarar a tuple, sempre acabar com , antes do parenteses.

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#Acesso direto

frutas[0] #laranja
frutas[2] #uva

#Índices negativos

frutas[-1] #uva
frutas[-3] #laranja

#Tuplas aninhadas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

#Primeiro [] seleciona a linha e a segunda [] seleciona o indice da tupla.
matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"


# Fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

# [Inicio:Fim:Step]
print(tupla[2:]) #('t', 'h', 'o', 'n')
print(tupla[:2]) #('p', 'y')
print(tupla[1:3]) #('y', 't')
print(tupla[0:3:2]) #('p', 't')
print(tupla[::]) #('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) #('n', 'o', 'h', 't', 'y', 'p')


#Iterar tuplas

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

#Função enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#0: gol
#1: celta
#2: palio

# ().count
# Conta a quantidade iguais de elementos na tupla
cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# ().index
# Informa o indice do elemento na tupla

linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java") # 3
linguagens.index("python") #0

# len()
# Conta quantos elementos tem na tupla

len(linguagens) # 5