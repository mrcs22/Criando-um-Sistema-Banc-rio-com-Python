import datetime

DAILY_WITDRAWS_LIMIT = 3 
WITDRAW_MONEY_LIMIT = 500

OPERATIONS = {
    'deposit': 'depósito',
    'withdraw': 'saque'
}

def deposit(accounts):
    account_number = input("Digite o número da conta: ")
    account = next((a for a in accounts if a['number'] == account_number), None)
    if not account:
        print("Conta não encontrada!")
        return

    valueToDeposit = 0

    try:
        valueToDeposit = float(input("Digite o valor do depósito: ").replace(',', '.'))
    except:
        print("Valor inválido!")
        return
    
    if valueToDeposit <= 0:
        print("Valor inválido!")
        return
    
    account['balance'] += valueToDeposit

    currentDate = datetime.datetime.now()
    account['operations'].append({
        'type': OPERATIONS['deposit'],
        'value': valueToDeposit, 
        'date': currentDate.strftime('%d/%m/%Y'),
        'time': currentDate.strftime('%H:%M:%S')
    })

    print(f"Depósito de R${valueToDeposit: .2f} realizado com sucesso!")

def show_statement(accounts):
    account_number = input("Digite o número da conta: ")
    account = next((a for a in accounts if a['number'] == account_number), None)
    if not account:
        print("Conta não encontrada!")
        return

    print("Extrato bancário")
    print(f"Saldo: R${account['balance']: .2f}")
    print("Operações realizadas:")

    if(len(account['operations']) == 0):
        print("Nenhuma operação realizada!")
        return
    
    for operation in account['operations']:
        print('-' * 30)
        print(f"""    
        Tipo: {operation['type']}
        Valor: R${operation['value']: .2f}
        Data: {operation['date']}
        Hora: {operation['time']}
        """)

def withdraw(accounts):
    account_number = input("Digite o número da conta: ")
    account = next((a for a in accounts if a['number'] == account_number), None)
    if not account:
        print("Conta não encontrada!")
        return

    withdraws_today = 0
    currentDate = datetime.datetime.now().strftime('%d/%m/%Y')
   
    for operation in account['operations']:
        if operation['type'] == OPERATIONS['withdraw'] and operation['date'] == currentDate:
            withdraws_today += 1
            
    if  withdraws_today >= DAILY_WITDRAWS_LIMIT:
        print("Limite diário de saques atingido!")
        return

    valueToWithdraw = 0
    try:
        valueToWithdraw = float(input("Digite o valor do saque: ").replace(',', '.'))
    except:
        print("Valor inválido!")
        return

    if valueToWithdraw <= 0:
        print("Valor inválido!")
        return
    
    if valueToWithdraw > WITDRAW_MONEY_LIMIT:
        print(f"Valor máximo para saque é de R${WITDRAW_MONEY_LIMIT: .2f}")
        return

    if valueToWithdraw > account['balance']:
        print("Saldo insuficiente!")
        return

    account['balance'] -= valueToWithdraw
    account['operations'].append({
        'type': OPERATIONS['withdraw'],
        'value': valueToWithdraw,
        'date': currentDate,
        'time': datetime.datetime.now().strftime('%H:%M:%S')
    })

    print(f"Saque de R${valueToWithdraw: .2f} realizado com sucesso!")

def register_user(users):
    user = {
        'name': '',
        'cpf': '',
        'birth_date': '',
        'address': {
            'street': '',
            'number': '',
            'neghborhood': '',
            'city': '',
            'state': ''
        }
    }
    
    cpf = input("Digite o CPF do usuário: ")
    only_numbers_cpf = ''.join(filter(str.isdigit, cpf))
    user['cpf'] = only_numbers_cpf

    conflicting_cpf_user = next((u for u in users if u['cpf'] == user['cpf']), None)
    if conflicting_cpf_user:
        print("CPF já cadastrado!")
        return
    
    user['name'] = input("Digite o nome do usuário: ")
    user['birth_date'] = input("Digite a data de nascimento do usuário: ")
    user['address']['street'] = input("Digite a rua do usuário: ")
    user['address']['number'] = input("Digite o número do usuário: ")
    user['address']['neghborhood'] = input("Digite o bairro do usuário: ")
    user['address']['city'] = input("Digite a cidade do usuário: ")
    user['address']['state'] = input("Digite o estado do usuário: ")
    
    users.append(user)
    print("Usuário cadastrado com sucesso!")

def list_users(users):
    if len(users) == 0:
        print("Nenhum usuário cadastrado!")
        return
    
    for user in users:
        print('-' * 30)
        print(f"""
        Nome: {user['name']}
        CPF: {user['cpf']}
        Data de nascimento: {user['birth_date']}
        Endereço: {user['address']['street']} - {user['address']['number']} - {user['address']['neghborhood']} - {user['address']['city']} / {user['address']['state']}
        """)

def create_account(accounts, users):
    account = {
        'user': None,
        'number': '',
        'agency': '0001',
        'balance': 0,
        'operations': []
    }

    cpf = input("Digite o CPF do usuário: ")
    only_numbers_cpf = ''.join(filter(str.isdigit, cpf))

    user = next((u for u in users if u['cpf'] == only_numbers_cpf), None)
    if not user:
        print("Usuário não encontrado!")
        return
    
    account['user'] = user
    account['number'] = str(len(accounts) + 1).zfill(4)
    accounts.append(account)

    print(f"Conta {account['number']} criada com sucesso na agência {account['agency']}!")

def list_accounts(users, accounts):
    cpf = input("Digite o CPF do usuário: ")
    only_numbers_cpf = ''.join(filter(str.isdigit, cpf))

    user = next((u for u in users if u['cpf'] == only_numbers_cpf), None)
    if not user:
        print("Usuário não encontrado!")
        return
    
    user_accounts = [a for a in accounts if a['user'] == user]
    if len(user_accounts) == 0:
        print("Nenhuma conta encontrada!")
        return
    
    for account in user_accounts:
        print('-' * 30)
        print(f"""
        Usuário: {account['user']['name']}
        Número da conta: {account['number']}
        Agência: {account['agency']}
        Saldo: R${account['balance']: .2f}
        """)

MENU = """

[d] - Depositar
[e] - Extrato
[s] - Sacar
[c] - Cadastrar usuário
[l] - Listar usuários
[a] - Adicionar conta
[lc] - Listar contas
[q] - Sair

"""

def main():
    users = []
    accounts = []

    while(True):
        print(MENU)
        option = input("Escolha uma opção: ")

        if option == 'd':
            deposit(accounts=accounts)      
        elif option == 'e':
            show_statement(accounts=accounts) 
        elif option == 's':
            withdraw(accounts=accounts)
        elif option == 'c':
            register_user(users)
        elif option == 'l':
            list_users(users)
        elif option == 'a':
            create_account(accounts, users)
        elif option == 'lc':
            list_accounts(users, accounts)
        elif option == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()