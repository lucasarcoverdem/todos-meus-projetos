currentBalance = 0

def doDeposit():
    global currentBalance
    print('\n- - - D E P Ó S I T O - - -')
    
    try:
        quantity = float(input('\nQuanto você deseja depositar? R$'))
        if quantity > 0:
            currentBalance += quantity
            print(f'\nDepósito realizado com sucesso! Novo saldo: R${currentBalance:.2f}')
        else:
            print('\nValor inválido! O depósito deve ser maior que R$0.')
    except ValueError:
        print('\nErro! Digite um número válido.')

def viewCurrentBalance():
    print('\n- - - S A L D O - - -')
    print(f'\nSeu saldo atual é R${currentBalance:.2f}')

def doTransfer():
    global currentBalance
    print('\n- - - T R A N S F E R Ê N C I A - - -')
    destination = input('\nEmail do destinatário: ').strip()
    
    while True:
        try:
            amount = float(input('Quantia a ser transferida: R$'))
            if amount <= 0:
                print('\nValor inválido! A quantia deve ser maior que zero.')
            elif amount > currentBalance:
                print('\nSaldo insuficiente. Por favor, tente novamente!')
            else:
                currentBalance -= amount
                print(f'\nTransferência de R${amount:.2f} concluída para {destination}!')
                break
        except ValueError:
            print('\nErro! Digite um valor numérico válido.')

def doWithdraw():
    global currentBalance
    print('\n- - - S A Q U E - - -')
    
    try:
        amount = float(input('\nQuanto deseja sacar? R$'))
        if amount <= 0:
            print('\nValor inválido! O saque deve ser maior que R$0.')
        elif amount > currentBalance:
            print('\nSaldo insuficiente!')
        else:
            currentBalance -= amount
            print(f'\nSaque realizado com sucesso! Novo saldo: R${currentBalance:.2f}')
    except ValueError:
        print('\nErro! Digite um valor numérico válido.')

def doInvest():
    stocks = ['NVDA', 'AMZO34', 'IBOV', 'GOGL34', 'MSFT34']
    userStocks = []
    criptos = ['BTC', 'ETH', 'XRP']
    userCriptos = []

    def stockExchange():
        print('\n- - - B O L S A - - -')
        while True:
            menu = input('\n1 - Comprar ações\n2 - Vender ações\n3 - Voltar\n\n').strip()
            if menu == '1':
                print('\nAções disponíveis:', ', '.join(stocks))
                stockPurchased = input('Digite o nome da ação que deseja comprar: ').strip().upper()
                if stockPurchased in stocks:
                    userStocks.append(stockPurchased)
                    print(f'\nVocê comprou ações da {stockPurchased}!')
                else:
                    print('\nAção inválida!')
            elif menu == '2':
                if not userStocks:
                    print('\nVocê não possui ações para vender.')
                else:
                    print('\nSuas ações:', ', '.join(userStocks))
                    sale = input('Digite o nome da ação que deseja vender: ').strip().upper()
                    if sale in userStocks:
                        userStocks.remove(sale)
                        print(f'\nVocê vendeu ações da {sale}!')
                    else:
                        print('\nVocê não possui essa ação.')
            elif menu == '3':
                break
            else:
                print('\nOpção inválida!')
    
    def cripto():
        print('\n- - - C R I P T O M O E D A S - - -')
        while True:
            menu = input('\n1 - Comprar criptos\n2 - Vender criptos\n3 - Voltar\n\n').strip()
            if menu == '1':
                print('\nCriptomoedas disponíveis:', ', '.join(criptos))
                criptoPurchased = input('Digite o nome da criptomoeda que deseja comprar: ').strip().upper()
                if criptoPurchased in criptos:
                    userCriptos.append(criptoPurchased)
                    print(f'\nVocê comprou {criptoPurchased}!')
                else:
                    print('\nCriptomoeda inválida!')
            elif menu == '2':
                if not userCriptos:
                    print('\nVocê não possui criptos para vender.')
                else:
                    print('\nSuas criptomoedas:', ', '.join(userCriptos))
                    sale = input('Digite o nome da criptomoeda que deseja vender: ').strip().upper()
                    if sale in userCriptos:
                        userCriptos.remove(sale)
                        print(f'\nVocê vendeu {sale}!')
                    else:
                        print('\nVocê não possui essa criptomoeda.')
            elif menu == '3':
                break
            else:
                print('\nOpção inválida!')
    
    def viewInvest():
        print('\n- - - S E U S  I N V E S T I M E N T O S - - -')
        if userStocks:
            print('\nAções:', ', '.join(userStocks))
        else:
            print('\nNenhuma ação comprada!')
        if userCriptos:
            print('\nCriptomoedas:', ', '.join(userCriptos))
        else:
            print('\nNenhuma criptomoeda comprada!')
    
    while True:
        menu = input('\n1 - Bolsa de valores\n2 - Criptomoedas\n3 - Ver investimentos\n4 - Voltar\n\n').strip()
        if menu == '1':
            stockExchange()
        elif menu == '2':
            cripto()
        elif menu == '3':
            viewInvest()
        elif menu == '4':
            break
        else:
            print('\nOpção inválida!')

def main():
    print('- - - B A N C O  A R C O V E R D E - - -')
    while True:
        menu = input('\n1 - Depositar\n2 - Retirar\n3 - Transferir\n4 - Ver saldo\n5 - Investimentos\n6 - Sair\n\n').strip()
        if menu == '1':
            doDeposit()
        elif menu == '2':
            doWithdraw()
        elif menu == '3':
            doTransfer()
        elif menu == '4':
            viewCurrentBalance()
        elif menu == '5':
            doInvest()
        elif menu == '6':
            print('\nEncerrando...')
            break
        else:
            print('\nOpção inválida!')

main()
