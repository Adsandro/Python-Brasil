altura = float(input('Informe sua altura em metros: '))
pesoIdeal = (72.7*altura) - 58


if __name__ == '__main__':
    print(f'seu peso ideal é de {round(pesoIdeal, 2)} Kg' .format(pesoIdeal))

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
