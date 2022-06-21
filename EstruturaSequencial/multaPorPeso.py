from unicodedata import decimal


pesoDoPeixe = float(input('Informe o peso do peixe: '))
limite = 50
multa = 4.00

if pesoDoPeixe > limite:
    excedente = pesoDoPeixe - limite
    valorMulta = excedente * multa
    print(f'O valor da multa é de {round(valorMulta, 2)},R$ pelo excedente de {round(excedente, 2)} Kg de peixe pela pesca realizada'.format(valorMulta, excedente))
else:
    print('Não ha multa estabelecida!!')

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.