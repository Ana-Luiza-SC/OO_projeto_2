from math import pi, sqrt, isclose

class Formas():
    def __init__(self, nome, lados: int):
        self._nome = nome
        self._lados = lados
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_lados(self, lados):
        if isinstance(lados, int):
            self._lados = lados
        else:
            print("Lados deve ser um inteiro.")
    
    def get_nome(self):
        return self._nome
    
    def get_lados(self):
        return self._lados
    
    def model(self):
        print(f'O nome da nome é {self.get_nome()} e tem {self.get_lados()} lados.')

class Ponto():
    def __init__(self, nome, x: float, y: float):
        self._nome = nome
        self._pos_x = x
        self._pos_y = y

    def set_x(self, x):
        if isinstance(x, (float, int)) and x >= 0:
            self._pos_x = float(x)
        else:
            print('Parâmetro inválido')
    
    def set_y(self, y):
        if isinstance(y, (float, int)) and y >= 0:
            self._pos_y = float(y)
        else:
            print('Parâmetro inválido')
            
    def set_nome(self, nome):
        if isinstance(nome, (Formas, str)):
            self._nome = nome
        else:
            print("Parâmetro inválido")

    def get_nome(self):
        return self._nome

    def get_x(self):
        return self._pos_x

    def get_y(self):
        return self._pos_y

    def distancia_origem(self) -> float:
        return sqrt((self._pos_x)**2 + (self._pos_y)**2)
    
    def model(self):
        print(f'Os parâmetros do ponto são: x= {self._pos_x} e y= {self._pos_y}')
    
    def verificacao_quadrante(self):
        if (self._pos_x >= 0 and self._pos_y >= 0):
            print(f'Ele se encontra no primeiro quadrante')
            return True
        else:
            print(f'Ele está fora do primeiro quadrante, x= {self._pos_x} e y= {self._pos_y}')
            return False

class SegmentoReta():
    def __init__(self, nome, ponto1: Ponto, ponto2: Ponto):
        self._nome = nome
        self._ponto1 = ponto1
        self._ponto2 = ponto2
        
    def set_ponto1_x(self, x):
        self._ponto1.set_x(x)
        
    def set_ponto1_y(self, y):
        self._ponto1.set_y(y)
        
    def set_ponto2_x(self, x):
        self._ponto2.set_x(x)
        
    def set_ponto2_y(self, y):
        self._ponto2.set_y(y)
            
    def set_nome(self, nome):
        self._nome = nome
            
    def get_nome(self):
        return self._nome

    def get_ponto1_x(self):
        return self._ponto1.get_x()

    def get_ponto1_y(self):
        return self._ponto1.get_y()
        
    def get_ponto2_x(self):
        return self._ponto2.get_x()
        
    def get_ponto2_y(self):
        return self._ponto2.get_y()
    
    def model(self):
        ponto1 = self._ponto1
        ponto2 = self._ponto2
        print(f'Os parâmetros da minha reta são: a=({ponto1.get_x()},{ponto1.get_y()}) e b=({ponto2.get_x()},{ponto2.get_y()})')
    
    def tamanho_reta(self):
        distancia = sqrt((self._ponto2.get_x() - self._ponto1.get_x()) ** 2 + (self._ponto2.get_y() - self._ponto1.get_y()) ** 2)
        return distancia

    def calcular_inclinacao(self) -> float:
        if self._ponto2.get_x() - self._ponto1.get_x() != 0:
            return (self._ponto2.get_y() - self._ponto1.get_y()) / (self._ponto2.get_x() - self._ponto1.get_x())
        else:
            return 0

class Circulo():
    def __init__(self, nome, x, y, raio):
        self._nome = nome
        self._centro = Ponto(nome, x, y)
        self._raio = raio
        
    def get_nome(self):
        return self._nome
        
    def get_raio(self):
        return self._raio
    
    def get_centro_x(self):
        return self._centro.get_x()
    
    def get_centro_y(self):
        return self._centro.get_y()
    
    def set_nome(self, nova_nome):
        self._nome = nova_nome
    
    def set_raio(self, r):
        if isinstance(r, (float, int)) and r > 0:
            self._raio = float(r)
        else:
            print('Parâmetro inválido')
        
    def set_x(self, x):
        self._centro.set_x(x)
            
    def set_y(self, y):
        self._centro.set_y(y)
    
    def model(self):
        print(f'O circulo possui centro em ({self.get_centro_x()}, {self.get_centro_y()}) e raio = {self.get_raio()}')
    
    def distancia_centro_origem(self):
        print(f'A distância entre o centro do círculo e a origem é {self._centro.distancia_origem():.2f}')
        
    def area(self) -> float:
        return pi * (self._raio ** 2)

class Retangulo():
    def __init__(self, nome, x: float, y: float, tam_altura, tam_comprimento):
        self._nome = nome
        self._Ponto = Ponto(nome, x, y)
        self._altura = tam_altura
        self._comprimento = tam_comprimento
        
    def get_Ponto_x(self):
        return self._Ponto.get_x()
    
    def get_Ponto_y(self):
        return self._Ponto.get_y()
    
    def set_nome(self, nova_nome):
        self._nome = nova_nome
        
    def set_x(self, x):
        self._Ponto.set_x(x)
            
    def set_y(self, y):
        self._Ponto.set_y(y)
        
    def get_altura(self):
        return self._altura
    
    def get_comprimento(self):
        return self._comprimento
    
    def set_altura(self, altura):
        if isinstance(altura, (float, int)) and altura > 0:
            self._altura = float(altura)
        else:
            print('Parâmetro inválido')
        
    def set_comprimento(self, comprimento):
        if isinstance(comprimento, (float, int)) and comprimento > 0:
            self._comprimento = float(comprimento)
        else:
            print('Parâmetro inválido')
        
    def area(self) -> float:
        return self._altura * self._comprimento
    
    def diagonal(self):
        diag = sqrt((self._altura ** 2) + (self._comprimento ** 2))
        print(f'O valor da diagonal é igual a {diag:.2f}')
    
    def perimetro(self):
        perimetro = 2 * self._altura + 2 * self._comprimento
        print(f'O perímetro é igual a {perimetro}')

class Quadrado(Retangulo):  # herança
    def __init__(self, nome, x: float, y: float, tam_altura):
        super().__init__(nome, x, y, tam_altura, tam_altura)
    
    def get_lado(self):
        return self._altura
        
    def set_altura(self, altura):
        if isinstance(altura, (float, int)) and altura > 0:
            self._altura = float(altura)
            self._comprimento = float(altura)
        else:
            print('Parâmetro inválido')
            
    def set_comprimento(self, comprimento):
        if isinstance(comprimento, (float, int)) and comprimento > 0:
            self._altura = float(comprimento)
            self._comprimento = float(comprimento)
        else:
           print('Parâmetro inválido')
        
    def set_lado(self, lado):
        if isinstance(lado, (float, int)) and lado > 0:
            self._altura = float(lado)
            self._comprimento = float(lado)
        else:
           print('Parâmetro inválido')
        
    def verificacao_quadrado(self):
        if self._altura == self._comprimento:
            return True
        else:
            return False
    
    def area(self) -> float:
        return self.get_altura() ** 2
    
class Triangulo():
    def __init__(self, nome, ponto_1: Ponto, ponto_2: Ponto, ponto_3: Ponto):
        self._nome = nome
        self._ponto1 = ponto_1
        self._ponto2 = ponto_2
        self._ponto3 = ponto_3
        self._lado1 = SegmentoReta(nome, ponto_1, ponto_2)
        self._lado2 = SegmentoReta(nome, ponto_2, ponto_3)
        self._lado3 = SegmentoReta(nome, ponto_1, ponto_3)
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nova_nome):
        self._nome = nova_nome
    
    def get_lado1(self):
        return self._lado1
    
    def get_lado2(self):
        return self._lado2
    
    def get_lado3(self):
        return self._lado3
    
    def set_ponto1_x(self, x):
        self._ponto1.set_x(x)
        self._update_segmentos()
    
    def set_ponto1_y(self, y):
        self._ponto1.set_y(y)
        self._update_segmentos()

    def set_ponto2_x(self, x):
        self._ponto2.set_x(x)
        self._update_segmentos()

    def set_ponto2_y(self, y):
        self._ponto2.set_y(y)
        self._update_segmentos()

    def set_ponto3_x(self, x):
        self._ponto3.set_x(x)
        self._update_segmentos()

    def set_ponto3_y(self, y):
        self._ponto3.set_y(y)
        self._update_segmentos()

    def _update_segmentos(self):
        self._lado1 = SegmentoReta(self._nome, self._ponto1, self._ponto2)
        self._lado2 = SegmentoReta(self._nome, self._ponto2, self._ponto3)
        self._lado3 = SegmentoReta(self._nome, self._ponto1, self._ponto3)

    def model(self):
        lado1 = self._lado1.tamanho_reta()
        lado2 = self._lado2.tamanho_reta()
        lado3 = self._lado3.tamanho_reta()
        print(f'O triângulo possui os seguintes tamanhos de lados: {lado1:.2f}, {lado2:.2f}, {lado3:.2f}')

    def is_triangulo(self):
        lado1 = self._lado1.tamanho_reta()
        lado2 = self._lado2.tamanho_reta()
        lado3 = self._lado3.tamanho_reta()
        
        return lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2
    
    def area(self) -> float:
        if self.is_triangulo():
            lado1 = self._lado1.tamanho_reta()
            lado2 = self._lado2.tamanho_reta()
            lado3 = self._lado3.tamanho_reta()
            s = (lado1 + lado2 + lado3) / 2
            return sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
        else:
            print("Os lados fornecidos não formam um triângulo.")
            return 0

class TrianguloRetangulo(Triangulo):
    def __init__(self, nome, ponto_1: Ponto, ponto_2: Ponto, ponto_3: Ponto):
        super().__init__(nome, ponto_1, ponto_2, ponto_3)
    
    def is_retangulo(self):
        if self.is_triangulo():
            lado1 = self._lado1.tamanho_reta()
            lado2 = self._lado2.tamanho_reta()
            lado3 = self._lado3.tamanho_reta()
            lados = sorted([lado1, lado2, lado3])
            return isclose(lados[0]**2 + lados[1]**2, lados[2]**2)
        else:
            return False

