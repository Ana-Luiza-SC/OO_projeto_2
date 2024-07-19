from package.maths.encapsulamento import Ponto,SegmentoReta,Circulo,Retangulo,Quadrado,Triangulo,TrianguloRetangulo
from package.maths.CartesianBoard import CartesianBoard


class Menu:
    def __init__(self):
        self.dashboard = CartesianBoard()
        
    def criacao_formas(self):
        
        while True:

            print("""Digite o número que está na frente da forma que você deseja criar:
    1. Ponto
    2. Segmento de reta
    3. Circulo
    4. Retângulo
    5. Quadrado
    6. Triângulo
    7. Triângulo retângulo""")
            
            try:
                verificacao = int(input('Digite o número da forma desejada: '))
                if verificacao>0 and verificacao<8:
                    break
        
            except :
                print('Entrada inválida. Digite um número.')

        if verificacao == 1:
            
            print('Vamos criar o Ponto!')
            nome = input('Escreva o nome do seu ponto: ')
            
            while True:
                try:
                    nome = input('Escreva o nome do segmento de reta: ')
                    x1, y1 = map(float, input('Escreva as coordenadas do ponto 1 (separadas por espaço): ').split())
                    x2, y2 = map(float, input('Escreva as coordenadas do ponto 2 (separadas por espaço): ').split())
                    ponto1 = Ponto(nome + "_1", x1, y1)
                    ponto2 = Ponto(nome + "_2", x2, y2)
                    meu_segmento = SegmentoReta(nome, ponto1, ponto2)
                    self.dashboard.criar_forma(meu_segmento)
                    break
                except:
                    print('Parâmetros inválidos para os pontos. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break
                        
        elif verificacao == 2:
            
            print('Vamos criar o Segmento de Reta!')
            nome = input('Escreva o nome do segmento de reta: ')
            
            try:
                x1, y1 = map(float, input('Digite as coordenadas do ponto 1 (x y): ').split())
                x2, y2 = map(float, input('Digite as coordenadas do ponto 2 (x y): ').split())
                
                ponto1 = Ponto(nome, x1, y1)
                ponto2 = Ponto(nome, x2, y2)
                
                meu_segmento = SegmentoReta(nome, ponto1, ponto2)
                self.dashboard.criar_forma(meu_segmento)
                
            except:
                print('Coordenadas inválidas.')
                
        elif verificacao == 3:
            
            print('Vamos criar o Círculo!')
            nome = input('Escreva o nome do círculo: ')
            
            while True:
                
                try:
                    x, y = map(float, input('Escreva as coordenadas do centro (separadas por espaço): ').split())
                    raio = float(input('Escreva o raio do círculo: '))
                    
                    meu_circulo = Circulo(nome, x, y, raio)
                    self.dashboard.criar_forma(meu_circulo)
                    break
                
                except:
                    print('Parâmetros inválidos para o círculo. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break

        elif verificacao == 4:
            
            print('Vamos criar o Retângulo!')
            nome = input('Escreva o nome do retângulo: ')
            
            while True:
                try:
                    x, y = map(float, input('Escreva as coordenadas do canto inferior esquerdo (separadas por espaço): ').split())
                    altura = float(input('Escreva a altura do retângulo: '))
                    comprimento = float(input('Escreva o comprimento do retângulo: '))
                    
                    meu_retangulo = Retangulo(nome, x, y, altura, comprimento)
                    self.dashboard.criar_forma(meu_retangulo)
                    break
                
                except:
                    print('Parâmetros inválidos para o retângulo. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break

        elif verificacao == 5:
            
            print('Vamos criar o Quadrado!')
            nome = input('Escreva o nome do quadrado: ')
            
            while True:
                
                try:
                    x, y = map(float, input('Escreva as coordenadas do canto inferior esquerdo (separadas por espaço): ').split())
                    lado = float(input('Escreva o tamanho do lado do quadrado: '))
                    
                    meu_quadrado = Quadrado(nome, x, y, lado)
                    self.dashboard.criar_forma(meu_quadrado)
                    break
                
                except:
                    print('Parâmetros inválidos para o quadrado. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break

        elif verificacao == 6:
            
            print('Vamos criar o Triângulo!')
            nome = input('Escreva o nome do triângulo: ')
            
            while True:
                
                try:
                    x1, y1 = map(float, input('Escreva as coordenadas do ponto 1 (separadas por espaço): ').split())
                    x2, y2 = map(float, input('Escreva as coordenadas do ponto 2 (separadas por espaço): ').split())
                    x3, y3 = map(float, input('Escreva as coordenadas do ponto 3 (separadas por espaço): ').split())
                    
                    ponto1 = Ponto(nome + "_1", x1, y1)
                    ponto2 = Ponto(nome + "_2", x2, y2)
                    ponto3 = Ponto(nome + "_3", x3, y3)
                    
                    meu_triangulo = Triangulo(nome, ponto1, ponto2, ponto3)
                    self.dashboard.criar_forma(meu_triangulo)
                    break
                
                except:
                    print('Parâmetros inválidos para os pontos. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break

        elif verificacao == 7:
            
            print('Vamos criar o Triângulo retângulo!')
            nome = input('Escreva o nome do triângulo retângulo: ')
            
            while True:
                
                try:
                    nome = input('Escreva o nome do triângulo retângulo: ')
                    x1, y1 = map(float, input('Escreva as coordenadas do ponto 1 (separadas por espaço): ').split())
                    x2, y2 = map(float, input('Escreva as coordenadas do ponto 2 (separadas por espaço): ').split())
                    x3, y3 = map(float, input('Escreva as coordenadas do ponto 3 (separadas por espaço): ').split())
                    
                    ponto1 = Ponto(nome + "_1", x1, y1)
                    ponto2 = Ponto(nome + "_2", x2, y2)
                    ponto3 = Ponto(nome + "_3", x3, y3)
                    
                    meu_triangulo_retangulo = TrianguloRetangulo(nome, ponto1, ponto2, ponto3)
                    self.dashboard.criar_forma(meu_triangulo_retangulo)
                    break
                
                except:
                    print('Parâmetros inválidos para os pontos. Tente novamente.')
                    saida = input('Deseja sair? (s/n): ').lower()
                    if saida == 's':
                        break
                

        
    def run(self):
        while True:
            try:
                print("""Escolha uma das seguintes opções:
    1. Criar uma forma geométrica
    2. Remover uma forma geométrica
    3. Verificar intersecção
    4. Sair""")
                
                saida = int(input('Escreva a opção escolhida: '))
                
                if saida == 1:
                    self.criacao_formas()
                elif saida == 4:
                    print('Saindo do programa')
                    break
                else:
                    print('Opção inválida! Escolha um número de 1 a 4.')
                
            except:
                print('Ocorreu algum erro, escreva apenas um número, referente às opções.')
                

