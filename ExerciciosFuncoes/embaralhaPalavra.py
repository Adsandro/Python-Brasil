from random import shuffle
palavra = input(str('Informe uma palavra'))

def embaralha(palavra):
    lista = list(palavra)
    shuffle(lista)
    lista = ''.join(lista)
    print(lista.lower())
    print(type(lista))
    
embaralha(palavra)
