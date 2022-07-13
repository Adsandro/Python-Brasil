dia = int(input('Informe um dia em numero '))
while dia <=0  or dia > 31:
    dia = int(input('Informe um dia em numero '))

mes = int(input('Informe o mês '))
while mes <= 0 or mes > 12:
    mes = int(input('Informe o mês '))

ano = int(input('Informe o ano '))
ano = str(ano)
while len(ano) < 4:
    ano = int(input('Informe o ano '))
    ano = str(ano)

print('A data informa é {}/{}/{}' .format(dia, mes, ano))

def data(dia, mes, ano):
    print(dia, 'de', mes, 'de', ano)
  
mesExtenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for i in range(mes):
    mesTemp = mesExtenso[i]

data(dia, mesTemp, ano)