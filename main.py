import datetime

DAILY_WITDRAWS_LIMIT = 3 
WITDRAW_MONEY_LIMIT = 500

balance = 0
operations = []

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
        'type': 'deposit',
        'value': valueToDeposit,
        'timestamp': datetime.datetime.now()
    })

    print(f"Depósito de R${valueToDeposit: .2f} realizado com sucesso!")

MENU = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[s] - Sair

"""

def main():
    while(True):
        print(MENU)
        option = input("Escolha uma opção: ")

        if option == 'd':
            deposit()       
        elif option == 's':
            print("Saindo...")
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()