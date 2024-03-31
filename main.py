import datetime

DAILY_WITDRAWS_LIMIT = 3 
WITDRAW_MONEY_LIMIT = 500

balance = 0
operations = []

OPERATIONS = {
    'deposit': 'depósito',
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
    operations.append({
        'type': OPERATIONS['deposit'],
        'value': valueToDeposit,
        'timestamp': datetime.datetime.now()
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
        data: {operation['timestamp'].strftime('%d/%m/%Y')}
        hora: {operation['timestamp'].strftime('%H:%M:%S')}
        """)

MENU = """

[d] - Depositar
[e] - Extrato
[s] - Sacar
[s] - Sair

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
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()