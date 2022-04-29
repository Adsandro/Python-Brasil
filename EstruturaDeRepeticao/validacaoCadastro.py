nome = input("Infome o nome do usuario: ")
len(nome)
while len(nome) < 4:
    nome = input("Informe um valor valido: ")

    
idade = int(input("Informe a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Informe uma idade valida, entre 0 e 150 anos: "))


salario = float(input("Salario em reais: "))
while salario < 0:
    salario = float(input("Informe um salario valido, maior que 0: "))


sexo = str(input("Informe o seu sexo com a primeira letra dele: "))
f = "feminino"
m = "masculino"
while sexo != "f" and sexo != "m":
    sexo = str(input("Informe o seu sexo com a primeira letra dele: "))


estadoc = str(input("Informe a primeira letra do seu estado civil: "))
s = "solteiro(a)"
c = "casado(a)"
v = "viuvo(a)"
d = "divorciado(a)"
while estadoc != "s" and estadoc != "c" and estadoc != "v" and estadoc != "d":
    estadoc = str(input("informe um estado civil valido: "))


print("valores corretos, obrigado !!")



