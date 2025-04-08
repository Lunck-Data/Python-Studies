menu = """
==========Opções Bancárias==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
====================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito=float(input("Valor do deposito: "))
        if deposito < 0:
                print("Valor inválido, insira um valor válido.")
                continue
        saldo += deposito
        print(f"Valor de R$ {deposito:.2f} depositado na conta")
        extrato = extrato + f"Valor de {deposito:.2f} depositado da conta\n"
        deposito = 0

    elif opcao == "2":
        print("Saque")
        saque = float(input("Valor de saque: "))
        if LIMITE_SAQUES == 0:
            print("Limite diario de 3 saques realizado")
            extrato = extrato + f"Limite de 3 saques diario - CONTA BLOQUEADA"
            continue
        if saque > 500:
            print("""
                                Saque Invalido
                  Limite de R$ 500,00 por saque diario ultrapassado""")
            continue
        if saque > saldo:
            print("""
                            Saque Invalido
                  Saque maior que saldo atual""")
            continue
        saldo -= saque
        extrato = extrato + f"Valor de {saque:.2f} retirado da conta\n"
        print(f"Saque de R$ {saque:.2f} realizado com sucesso")
        LIMITE_SAQUES -= 1
        saque = 0

    elif opcao == "3":
        print(extrato)
        print(f"Valor na conta de R${saldo:.2f}")

    elif opcao == "0":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

print(saldo)





#                                       Operação de depósito
# Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
# dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos
# devem ser armazenados em uma variável e exibidos na operação de extrato.

#                                         Operação de saque
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo
# em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os
# saques ser armazenados em uma variável e exibidos na operação de extrato.

#                                       Operação de extrato
# Essa operação deve lista todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizar o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1.500,45