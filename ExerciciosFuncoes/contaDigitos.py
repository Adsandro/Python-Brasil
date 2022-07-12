def contaDigitos(numero):
    string = str(numero)
    print('O numero informado possui {} digitos.' .format(len(string)))
    
    
n = int(input('Informe um numero inteiro: '))
contaDigitos(n)