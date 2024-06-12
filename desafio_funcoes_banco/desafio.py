def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if saldo != 0 and (numero_saques < LIMITE_SAQUES):
        if valor <= saldo and valor <= limite:
            saldo -= valor
            extrato.append(f'Saque de R$ {valor:.2f}\n') 
            return saldo, extrato
        else:
           print(f'O valor de saque não pode ser maior que R$ 500.00')
           return saldo, extrato
    elif numero_saques == LIMITE_SAQUES:
        print(f'Você atingiu o limite de 3 saques diários!')
        return saldo, extrato
    else:
        print(f'Você não possui nenhum valor em sua conta para sacar.\n\nSaldo: R$ {saldo:.2f}')
        return saldo, extrato
    

def deposito(saldo, valor, extrato, /):
    saldo += valor
    extrato.append(f'Deposito de R$ {valor:.2f}\n')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    if extrato == []:
            print("Não foram realizadas movimentações.")
    else:
        extrato_extenso = "\n".join(extrato)
        print(f'{extrato_extenso}\n Saldo: R${saldo}')


def data_nascimento():
    dia = input("Digite o dia de seu nascimento: ")
    mes = input("Digite o mes (em números 1-12) de seu nascimento: ")
    ano = input("Digite o ano de seu nascimento: ")
    return f'{dia}/{mes if len(mes) == 2 else ("0" + mes)}/{ano}'


def endereco():
    logradouro = input("Digite o nome da rua onde mora: ")
    numero_da_casa = input("Digite o número de sua casa: ")
    bairro = input("Digite o nome de seu bairro: ")
    cidade = input("Digite o nome de sua cidade: ")
    estado = input("Digite a sigla de seu estado (Ex: SP, RJ...): ")
    return f'{logradouro.title()}, {numero_da_casa} - {bairro.title()} - {cidade.title()}/{estado.upper()}'
    

def arrumar_cpf(cpf):
    numeros_cpf = ""
    for numero in cpf:
        if numero.isdecimal():
            numeros_cpf += numero
    return numeros_cpf
    
    
def checar_cpf(cpf, lista_usuarios):
    cpf_duplicado = False
    for i, item in enumerate(lista_usuarios):
        if cpf in item:
            cpf_duplicado = True
    return cpf_duplicado
    
    
def criar_usuario(lista_usuarios):
    cpf = input("Digite o seu CPF: ")
    cpf = arrumar_cpf(cpf)
    cpf_duplicado = checar_cpf(cpf, lista_usuarios)
    if cpf_duplicado:
        print(f'Impossível criar outro usuário. CPF já consta no sistema!')
        return
    nome_completo = input("Por favor, digite o seu nome completo: ")
    data_de_nascimento = data_nascimento()
    endereco_completo = endereco()
    return [nome_completo.capitalize(), data_de_nascimento, cpf, endereco_completo]


def listar_usuarios(lista_usuarios, tipo=None):
    if lista_usuarios == []:
        print("Não existe usuários cadastrados!")
    elif tipo == "escolher":
        count_indices = []
        for i, item in enumerate(lista_usuarios):
            print(f'Indice: {i} - {item[0]} | {item[2]}')
            count_indices.append(i)
        indice_usuario = int(input("Escolha o usuário desejado para criar a conta (0, 1, 2,...): "))
        
        if indice_usuario in count_indices:
            usuario_escolhido = lista_usuarios[indice_usuario]
            return usuario_escolhido
        else:
            print("Indice selecionado não existe!")
    else:
        for usuario in lista_usuarios:
            usuario_extenso = ""
            for i in usuario:
                usuario_extenso += f"{i}| "
            print(usuario_extenso)


def criar_conta_corrente(numero_conta):
    usuario = listar_usuarios(lista_usuarios, 'escolher')
    AGENCIA = "0001"
    numero_da_conta = numero_conta
    numero_conta += 1
    contas.append(f'Agencia: {AGENCIA}, Número da Conta: {numero_da_conta}, Usuario: {usuario[0]}')
    
    return contas, numero_conta


def listar_contas_correntes(contas):
    if contas == []:
        print('Não existem contas correntes criadas!')
        return
    for item in contas:
        print(item)


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Conta Corrente
[u] Criar usuário
[l] Listar usuários
[p] Listar Contas Correntes
[q] Sair

=> """


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
contas = []
numero_conta = 1

while True:
    

    opcao = input(menu)

    print()
    
    if opcao.lower() == "d":
        valor = float(input("Digite o valor do deposito: "))
        saldo, extrato = deposito(saldo, valor, extrato)
    elif opcao.lower() == "s":
        valor = float(input("Digite o valor que deseja sacar: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        numero_saques += 1
    elif opcao.lower() == "e":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao.lower() == "c":
        contas, numero_conta = criar_conta_corrente(numero_conta)
    elif opcao.lower() == "u":
        usuario = criar_usuario(lista_usuarios)
        if usuario is not None:
            lista_usuarios.append(usuario)
    elif opcao.lower() == "l":
        listar_usuarios(lista_usuarios)
    elif opcao.lower() == "p":
        listar_contas_correntes(contas)
    elif opcao.lower() == "q":
        break
    
    else:
        print("Você não digitou uma opção correta. Por favor, tente novamente!")