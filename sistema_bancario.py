#Menu onde o usuário vai escolher o que ele vai fazer 
menu = """
Digite a inicial da ação que vc quer fazer
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valores negativos não são permitidos")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_saques == 1
        
        else:
            print("Operação falhou! Não são permitidos valores negativos")

    elif opcao == "e":
        print ("\n--------Extrato--------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------")
    
    elif opcao == "q":
        break

    else:
        print("Opreação inválida")
    