import math

def continuar():
    while True: 
        opcao = input('\n\nDeseja continuar? (s/n) ').strip().lower()
        if opcao in ['s', 'sim']:
            return True
        elif opcao in ['n', 'não', 'nao']:
            print('\nEncerrando...')
            return False
        else:
            print("Opção inválida! Digite 's' para continuar ou 'n' para sair.")

def operacoesBasicas():
    while True:
        try:
            num1 = float(input('\nInsira um número: '))
            num2 = float(input('Insira outro número: '))
        except ValueError:
            print("\nPor favor, insira números válidos.")
            continue

        operacao = input(
            '\nO que deseja fazer?\n\n'
            '1 - Somar\n'
            '2 - Subtrair\n'
            '3 - Multiplicar\n'
            '4 - Dividir\n'
            '0 - Voltar\n\n'
        ).strip().lower()

        if operacao in ['0', 'voltar']:
            break
        elif operacao in ['1', 'somar']:
            resultado = num1 + num2
        elif operacao in ['2', 'subtrair']:
            resultado = num1 - num2
        elif operacao in ['3', 'multiplicar']:
            resultado = num1 * num2
        elif operacao in ['4', 'dividir']:
            if num2 == 0:
                print("\nErro: Divisão por zero não é permitida.\n")
                continue
            resultado = num1 / num2
        else:
            print("\nOpção inválida. Tente novamente.")
            continue

        print(f'\nO resultado é: {resultado}')
        
        if not continuar():
            break

def circunferencia():
    while True:
        try:
            raio = float(input('\nInsira o raio do círculo: '))
            circunferencia = 2 * math.pi * raio
        except ValueError:
            print('\nInsira valores corretos!')
            continue

        preferencia = input(
            '\nExibir valor:\n'
            '1 - Total\n'
            '2 - Arredondado\n\n'
        ).strip().lower()

        if preferencia in ['1', 'total']:
            print(f'\nO resultado é: {circunferencia}')
        elif preferencia in ['2', 'arredondado']:
            print(f'\nO resultado é: {round(circunferencia)}')
        else:
            print("\nOpção inválida. Tente novamente.")
            continue

        if not continuar():
            break

def pitagoras():
    while True:
        try:
            a = float(input('\nInsira o cateto A: '))
            b = float(input('Insira o cateto B: ')) 
            hipotenusa = math.sqrt(pow(a, 2) + pow(b, 2))
        except ValueError:
            print('Insira valores corretos!')
            continue      

        preferencia = input(
            '\nExibir valor:\n'
            '1 - Total\n'
            '2 - Arredondado\n\n'
        ).strip().lower()

        if preferencia in ['1', 'total']:
            print(f'\nO resultado é: {hipotenusa}')
        elif preferencia in ['2', 'arredondado']:
            print(f'\nO resultado é: {round(hipotenusa)}')
        else:
            print("\nOpção inválida. Tente novamente.")
            continue

        if not continuar():
            break

def bhaskara():
    while True:
        try:
            a = float(input('\nInsira o coeficiente a: '))
            b = float(input('Insira o coeficiente b: '))
            c = float(input('Insira o coeficiente c: '))
            
            delta = b**2 - 4*a*c
            
            if delta < 0:
                print('\nA equação não possui raízes reais.')
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                
                print(f'\nAs raízes da equação são: x1 = {x1}, x2 = {x2}')
        except ValueError:
            print('\nInsira valores corretos!')
            continue

        if not continuar():
            break

def main():
    while True: 
        print('--- CALCULADORA ---\n')
        opcoes = input(
            '1 - Operações básicas\n'
            '2 - Circunferência do círculo\n'
            '3 - Teorema de Pitágoras\n'
            '4 - Fórmula de Bhaskara\n'
            '0 - Sair\n\n'
        ).strip().lower()

        if opcoes in ['0', 'sair']:
            print('Encerrando...')
            break
        elif opcoes in ['1', 'operações básicas']:
            operacoesBasicas()
        elif opcoes in ['2', 'circunferência', 'circunferência do círculo']:
            circunferencia()
        elif opcoes in ['3', 'teorema de pitágoras', 'pitágoras']:
            pitagoras()
        elif opcoes in ['4', 'fórmula de bhaskara', 'bhaskara']:
            bhaskara()
        else:
            print("\nOpção inválida. Tente novamente.")

main()
