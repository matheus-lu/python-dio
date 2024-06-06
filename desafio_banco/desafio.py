menu = """

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
    print()
    
    if opcao.lower() == "d":
        valor = float(input("Digite o valor do deposito: "))
        saldo += valor
        extrato += f'Deposito de R$ {valor:.2f}\n'
        
        
    elif opcao.lower() == "s":
        if saldo != 0 and (numero_saques < LIMITE_SAQUES):
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= saldo and valor <= 500:
                saldo -= valor
                extrato += f'Saque de R$ {valor:.2f}\n'
                numero_saques += 1
            else:
                print(f'O valor de saque não pode ser maior que R$ 500.00')
        elif numero_saques == LIMITE_SAQUES:
            print(f'Você atingiu o limite de 3 saques diários!')
        else:
            print(f'Você não possui nenhum valor em sua conta para sacar.\n\nSaldo: R$ {saldo:.2f}')

    elif opcao.lower() == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f'{extrato}\nSaldo: R${saldo}')
        
    elif opcao.lower() == "q":
        break
    
    else:
        print("Você não digitou uma opção correta. Por favor, tente novamente!")