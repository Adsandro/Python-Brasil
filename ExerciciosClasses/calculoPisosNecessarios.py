class retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def obterArea(self):
        area = self.x * self.y
        return area
    
    def obterPerimetro(self):
        perimetro = self.x * 2 + self.y * 2
        return perimetro
    
    
class local:
    def __init__(self, medidaX, medidaY):
        self.medidaX = medidaX
        self.medidaY = medidaY

    def obterAreaLocal(self):
        area = self.medidaX * self.medidaY
        return area
    
    
ladoX = float(input('Informe o valor do lado X do piso : '))
ladoY = float(input('Informe o valor do lado Y piso : '))
retangulo1 = retangulo(ladoX, ladoY)

medidaLocalX = float(input('Informe o valor X do local: '))
medidaLocalY = float(input('Informe o valor Y do local: '))
local1 = local(medidaLocalX, medidaLocalY)

print('Cada piso tera area de {}'.format(retangulo1.obterArea()))
print('E possuira perimetro de {}'.format(retangulo1.obterPerimetro()))

print('A area do local é de {}'.format(local1.obterAreaLocal()))

pisosNecessarios = local1.obterAreaLocal() / retangulo1.obterArea()

print('Serão necessarios {} pisos'.format(pisosNecessarios))





# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.