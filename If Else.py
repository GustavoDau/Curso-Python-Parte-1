# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint

computador = randint(0, 5)
n = int(input('Em que numero eu pensei?'))
if computador == n:
    print('Parabens voce acertou o numero correto')
else:
    print('voce errou tente novamente mais tarde')

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input('Digite a velocidade do carro'))
multa = 7
if km <= 80:
    print('Voce esta no dentro do limite de velocidade')
else:
    print(('Voce tera que paga uma multa de {}'.format((km - 80) * 7)))

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('digite um numero'))
resultado = numero % 2
if resultado == 0:
    print('o numero digitado eh par')
else:
    print('o numero digitado eh inpar')

# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('digite a distancia percorrida'))
if distancia < 200:
    print('o valor a ser pago pega viagem sera de {:.2f} reais'.format(distancia * 0.5))
else:
    print(('o valor a ser pago pela viagem sera de {:.2f} reais'.format(distancia * 0.45)))

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior numero digitado eh o {}'.format(maior))
print('o menor numero digitado eh o {}'.format(menor))

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('digite o salario'))
aumento1 = salario * 0.1
aumento2 = salario * 0.15
if salario > 1250:
    print('O seu salario com aumento vai ser de {:.2f} reais'.format(salario + aumento1))
else:
    print('O seu salario com aumento vai ser de {:.2f} reais'.format((salario + aumento2)))

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('digite o valor do primeiro lado'))
r2 = float(input('digite o valor do segundo lado'))
r3 = float(input('digite o valor do terceiro lado'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('pode ser criado um triangulo')
else:
    print(('nao pode ser criado um triangulo'))