#  1 Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. 
#    Se eles forem iguais, imprima que são valores idênticos.

#input
#numero1 = float(input("Digite um número: "))
#numero2 = float(input("Digite um número: "))

def numero_menor(numero1, numero2):
    if numero1 < numero2:
        return numero1
    elif numero1 == numero2:
        return "Identicos"
    else:
        return numero2

#print(f' O menor número é: {numero_menor(numero1, numero2)}')

# 2 Escreva uma função que recebe dois números (a e b) como 
#   parâmetro e retorna True caso a soma dos dois seja maior 
#   que um terceiro parâmetro, chamado limite.

# input
#numeroA = float(input("Digite um número: "))
#numeroB = float(input("Digite um número: "))
#limite = 20

# processamento

def resultado (numeroA, numeroB, limite):
    if numeroA + numeroB > limite:
        return True
    else:
        return False

#print (resultado(numeroA, numeroB, limite))

# 03 Crie uma função que receba uma string como argumento e retorne a 
# mesma string em letras maiúsculas. Faça uma chamada à função, 
# passando como parâmetro uma string.

#string = input('Digite uma algo: ')


def toUpper(string):
    return string.upper()


#print(toUpper(s))

# 4 Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de 
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.


#from datetime import datetime

#strDate = input('Digite o dia do seu nascimento: ')


def voto(dateVote):
    dataCerto = datetime.strptime(dateVote, '%d/%m/%Y')
    year = dataCerto.year
    if (2021 - year > 18):
        return 'Obrigatório'
    elif (2021 - year > 16):
        return 'Opicional'
    else:
        return 'Negado'



#print(voto(strDate))

# 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: 
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum 
# dado não tenha sido informado corretamente.

# input

#nomeJogador = input('Digite o nome do jogador: ')
#gols = input('Quantos gols ele marcou? ')


def ficha(player, gol):
    if len(player) == 0:
        return f'O jogador desconhecido fez {gol} gols na partida'
    elif len(gol) == 0:
        return f'O jogador {player} fez não fez gols na partida'
    else:
        return f'O jogador {player} fez {gol} gols na partida'


#(ficha(nomeJogador, gols))

#Exercício 6 Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as 
# duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 
# 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

#input
prova1 = float(input("Digite sua nota: "))
prova2 = float(input("Digite sua nota: "))
prova3 = float(input("Digite sua nota: "))

#processamento
def mediaDe3(prova1, prova2, prova3):
    mediaDe3 = (prova1 + prova2 + prova3) / 3
    return mediaDe3

def menor(prova1, prova2, prova3):
    if prova1 <= prova2 and prova1 <= prova3:
        return prova1
    if prova2 <= prova1 and prova2 <= prova3:
        return prova2
    if prova3 <= prova1 and prova3 <= prova2:
        return prova3

def maior(prova1, prova2, prova3):
    if prova1 >= prova2 and prova1 >= prova3:
        return prova1
    if prova2 >= prova1 and prova2 >= prova3:
        return prova2
    if prova3 >= prova1 and prova3 >= prova2:
        return prova3

media = ((prova1+prova2+prova3)- menor(prova1, prova2, prova3))/2
print("A média das duas provas com notas mais altas é: ", media)

print(f'A média das 3 provas é: {mediaDe3(prova1, prova2, prova3):.2f}')
print("A maior nota é: ", maior(prova1, prova2, prova3))
print("A menor nota é: ", menor(prova1, prova2, prova3))

#testando
print('Ola mundo')