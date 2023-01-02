#todas as letras em maiusculo,minusculo,letras aotodo sem espaco, e quantas letras tem o primeiro nome
nome = str(input('digite seu nome')).strip()
print('seu nome em letras maiusculas: {} '.format(nome).upper())
print('seu nome em letras minusculas: {} '.format(nome).lower())
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome: {} '.format(separa[0], len(separa[0])))

# ler uma frase e quantas vezes aparece a letra A, em que posicao aparece pela primeira vez e ultima vez

#leia o nome da cidade e veja se o nome comeca com santo.
cid = str(input('em que cidade voce nasceu')).strip()
print(cid[:5].upper() == 'SANTO')

# leia o nome de uma pessoa e veja se tem silva dentro do nome
nome = str(input('qual é o seu nome completo')).strip()
print('seu nome tem silva? {}'.format('SILVA' in nome.upper()))


#faca um programa q leia uma frase
#quantas vezes aparece a letra A
#em que posicao aparece pela primeira vez  e ultima vez - foi colocado o +1 pois a posicao 1 para o python eh 0

frase = str(input('digite uma frase')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira leta A foi achada na posicao {} '.format(frase.find('A')+1))
print('a ultima letra A foi achada na posicao {}'.format(frase.rfind('A')+1))

#faca um programa que leia o nome completo e mostre o primeiro e ultimo nome da pessoa
n = str(input('digite sue nome completo')).strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))