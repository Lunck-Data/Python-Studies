#Compreensão de listas
#Filtro versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

#.append() em Python adiciona um único elemento ao final de uma lista
for numero in numeros:
    if numero % 2 == 0: #Se atender é Par
        pares.append(numero)

#print(pares) # 30, 2, 34

#Filtro versão 2

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares) # 30, 2, 34




#Modificando valores versão 1
#Irá elevar os valores a quadrado

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2) #.append adiciona um valor ao final de uma lista.
print(quadrado) #[1, 900, 441, 4, 81, 4225, 1156]


#Modificando valores versão 2
#Irá elevar os valores a quadrado

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado) #[1, 900, 441, 4, 81, 4225, 1156]