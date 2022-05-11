pais1 = 80000
pais2 = 200000
taxaA = 0.03
taxaB = 0.015

xAnos = 0

while pais1 < pais2:
    pais1 = pais1 + (taxaA * pais1)
    pais2 = pais2 + (taxaB * pais2) 
    xAnos = xAnos + 1

print(xAnos)


# A = 80000
# B = 200000
# taxaA = 0.03
# taxaB = 0.015

# anos = 0
# while A < B:
#     A = A + (A * taxaA)
#     B = B + (B * taxaB)
#     anos = anos + 1
    
# print(anos)