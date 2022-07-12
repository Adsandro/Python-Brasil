def reverso(numero):
    numero = str(numero)    
    return numero[::-1] #Inverte o numero, u string

n = 2345
# n = input('Informe um numero para invertermos: ')
print(reverso(n))