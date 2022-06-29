from codecs import latin_1_decode


class quadrado:
    def __init__(self, lado):
        self.lado = lado
        print('lado = ',lado)
    def area(self):
        area = self.lado * self.lado
        print('area = ', area)

        
quadrado1 = quadrado(5)
quadrado1.area()




# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;