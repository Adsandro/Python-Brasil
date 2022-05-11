pais1 = int(input("Informe a população inicial do primeiro país:"))
pais2 = int(input("Informe a população inicial do segundo país:"))
taxaA = float(input("Informe a taxa de crescimento do primeiro paiís: "))
taxaB = float(input("Informe a taxa de crescimento do segundo paiís: "))

xAnos = 0

if pais1 < pais2:
    while pais1 < pais2:
        pais1 = pais1 + (taxaA * pais1)
        pais2 = pais2 + (taxaB * pais2) 
        xAnos = xAnos + 1
else:
    while pais1 > pais2:
        pais1 = pais1 + (taxaA * pais1)
        pais2 = pais2 + (taxaB * pais2) 
        xAnos = xAnos + 1
    

print(xAnos)

