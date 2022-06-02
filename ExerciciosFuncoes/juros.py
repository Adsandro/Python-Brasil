def valorTotal(valorPrestacao, diaAtraso):
    valor = float(valorPrestacao + (3/100 * valorPrestacao) + ((1/1000 * valorPrestacao) * diaAtraso))
    return valor
valorPrestacao = 1
while valorPrestacao != 0:
    valorPrestacao = float(input("Informe o valor da prestação: "))
    diaAtraso = int(input("Informe quantos dias estão atrasados: "))
    print(valorTotal(valorPrestacao, diaAtraso ))