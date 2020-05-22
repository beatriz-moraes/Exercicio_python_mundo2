'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep
cont = 0
sorteado =(randint(0, 10))
print('Você consegue adivinhar em qual número vou jogar, humano?')
while True:
    num = int(input('Escolha um número de 0 até 10: '))
    print('Processando...')
    sleep(3)

    if num < sorteado:
        print('E VOCÊ ERROU, TENTE NÚMERO MAIOR QUE ESSE!')
        cont += 1
        print('-------------------')

    elif num > sorteado:
        print('E VOCÊ ERROU, TENTE NÚMERO MENOR QUE ESSE!')
        cont += 1
        print('-------------------')

    if num == sorteado:
        print(f'E VOCÊ ACERTOU O NÚMERO SORTEADO É {sorteado}, PARABÉNS!!!')
        cont += 1
        print(f'Você Precisou de {cont} tentativas!')
        break