# for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# for/else
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

# range
# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
# [0, 1, 2, 3]

# Utilizando a função built-in range
for numero in range(0, 11):
    print(numero, end=" ")

print( )

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

print( )

# while
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato\n[0] Sair\n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# while/else
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato\n[0] Sair\n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário: até logo!")

while True:
    numero = int(input("Informe um número inteiro: \n10 Encerra."))

    if numero == 10:
        break

    print(numero)

for numero in range (10):

    if numero == 5:
        continue

    print(numero, end=" ")

print("Fim dos exemplos de laço de repetição")

