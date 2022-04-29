nome = str(input("Informe seu nome: "))
senha = str(input("Informe uma senha valida, diferente do nome de usúario: "))
while senha == nome: 
    senha = str(input("A senha corresponde ao nome do usúario, por favor informe uma senha valida: "))
print("A senha é valida!!")

'''caso a senha possua um caracter diferente, o teste é visto como valido '''
