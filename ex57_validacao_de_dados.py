'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto!'''

sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
while True:
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos! Por favor, digite seu sexo [M/F]: ')).strip().upper()[0]
    else:
        print(f'Sexo {sexo} registrado com sucesso!')
        break

