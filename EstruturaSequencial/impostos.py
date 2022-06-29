HorasTrabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês:'))
valorHora = float(input('Informe o valor da hora trabalhada: '))

salario = valorHora * HorasTrabalhadas
impostoDeRenda = salario * 11/100
Inss = salario * 8/100
sindicato = salario * 5/100
salarioLiquido = salario - impostoDeRenda - Inss - sindicato 

print('Com essas horas trabalhadas tera {} R$' .format(salario))
print('Para imposto de renda em {} R$' .format(impostoDeRenda) )
print('INSS de {} R$' .format(Inss))
print('{} R$ para o sindicato' . format(sindicato))
print('E terminara com salario liquido de {} R$' .format(salarioLiquido))


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo: