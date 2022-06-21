altura = float(input('Informe sua altura em metros: '))
sexo = input('Como o senhor(a) se define? Homem ou mulher?')
 
if sexo == 'homem':
    sexo = 'Homem'
else:
    sexo = 'mulher'

if sexo == 'Homem':
    pesoIdeal = (72.7*altura) - 58
    print(f'Com base em sua altura, o seu peso ideal é de {round(pesoIdeal, 2)}Kg')
elif sexo == 'mulher':
    pesoIdeal = (62.1*altura) - 44.7
    print(f'Com base em sua altura, o seu peso ideal é de {round(pesoIdeal, 2)}Kg')

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7