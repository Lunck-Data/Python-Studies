# if
saldo = 2000.0
saque = float(input("Informe o valo do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# if/else
saldo = 2000.0
saque = float(input("Informe o valo do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# if/elif/else
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato: \n"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")

# if aninhado
cheque_especial = 100
conta_normal = True
conta_universitaria = True

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

# if ternário
saldo = 1000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
