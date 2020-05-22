''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Qual a opção que vc escolhe: '))

while True:
    if opcao == 1 and opcao != 5:
        print(f'A soma dos dois valores da o resultado de : {num1 + num2}')
        print(30*'=')
        opcao = int(input('Qual a opção que vc escolhe: '))

    elif opcao == 2 and opcao != 5:
        print(f'A multiplicação dos dois números da o resultado de : {num1 * num2}')
        print(30 * '=')
        opcao = int(input('Qual a opção que vc escolhe: '))

    elif opcao == 3 and opcao != 5:
        if num1 > num2:
            print(f'O primeiro número digitado é o maior, o número {num1}')
            print(30 * '=')
            opcao = int(input('Qual a opção que vc escolhe1: '))
        else:
            print(f'O segundo número digitado é o maior, o número {num2}')
            print(30 * '=')
            opcao = int(input('Qual a opção que vc escolhe0: '))

    elif opcao == 4 and opcao != 5:
        print('Digite os números novamentes!')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(30 * '=')
        opcao = int(input('Qual a opção que vc escolhe: '))

    elif opcao == 5:
        print('Obrigada por ultilizar o programa da nossa empresa! Até mais!')
        break
    else:
        print('Digito inválido!')
        break



