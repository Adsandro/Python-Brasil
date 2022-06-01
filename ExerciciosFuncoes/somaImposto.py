def somaImposto(imp, val):
    valorTotal = int(val) + int((imp/100)*val)
    return valorTotal
print(somaImposto(15, 200))