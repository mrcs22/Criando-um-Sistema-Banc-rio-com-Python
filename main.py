import datetime

DAILY_WITDRAWS_LIMIT = 3 
WITDRAW_MONEY_LIMIT = 500

balance = 0
operations = []

OPERATIONS = {
    'deposit': 'depósito',
    'withdraw': 'saque'
}

def deposit():
    global balance
    valueToDeposit = 0

    try:
        valueToDeposit = float(input("Digite o valor do depósito: ").replace(',', '.'))
    except:
        print("Valor inválido!")
        return
    
    if valueToDeposit <= 0:
        print("Valor inválido!")
        return
    
    balance += valueToDeposit

    currentDate = datetime.datetime.now()
    operations.append({
        'type': OPERATIONS['deposit'],
        'value': valueToDeposit, 
        'date': currentDate.strftime('%d/%m/%Y'),
        'time': currentDate.strftime('%H:%M:%S')
    })

    print(f"Depósito de R${valueToDeposit: .2f} realizado com sucesso!")

def show_statement():
    print("Extrato bancário")
    print(f"Saldo: R${balance: .2f}")
    print("Operações realizadas:")

    if(len(operations) == 0):
        print("Nenhuma operação realizada!")
        return
    
    for operation in operations:
        print('-' * 30)
        print(f"""    
        Tipo: {operation['type']}
        Valor: R${operation['value']: .2f}
        Data: {operation['date']}
        Hora: {operation['time']}
        """)

def withdraw():
    global balance
    global operations

    withdraws_today = 0
    currentDate = datetime.datetime.now().strftime('%d/%m/%Y')
   
    for operation in operations:
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

    if valueToWithdraw > balance:
        print("Saldo insuficiente!")
        return

    balance -= valueToWithdraw
    operations.append({
        'type': OPERATIONS['withdraw'],
        'value': valueToWithdraw,
        'date': currentDate,
        'time': datetime.datetime.now().strftime('%H:%M:%S')
    })

    print(f"Saque de R${valueToWithdraw: .2f} realizado com sucesso!")

MENU = """

[d] - Depositar
[e] - Extrato
[s] - Sacar
[q] - Sair

"""

def main():
    while(True):
        print(MENU)
        option = input("Escolha uma opção: ")

        if option == 'd':
            deposit()      
        elif option == 'e':
            show_statement() 
        elif option == 's':
            withdraw()
        elif option == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()