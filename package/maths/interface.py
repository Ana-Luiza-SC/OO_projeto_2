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
                print('')
                if verificacao>0 and verificacao<8:
                    break
        
            except :
                print('Entrada inválida. Digite um número inteiro.')
                print('\n')

        if verificacao == 1:
            
            print('Vamos criar o Ponto!')
            print('')
            nome = input('Escreva o nome do seu ponto: ')
            
            while True:
                try:
                    x, y = map(float, input('Escreva as coordenadas do ponto maior ou igual a 0 (separadas por espaço): ').split())
                    
                    if x>=0 and y>=0:
                        meu_ponto = Ponto(nome, x,y)
                        self.dashboard.criar_forma(meu_ponto)
                        break
                    else:
                        print('A coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar criando o ponto? (s/n): ').lower()
                        print('')
                        if saida == 'n':
                            break
                except:
                    print('Parâmetros inválidos para o ponto.')
                    saida = input('Deseja continuar criando o ponto? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break
                        
        elif verificacao == 2:
            
            print('Vamos criar o Segmento de Reta!\n')
            print('')
            nome = input('Escreva o nome do segmento de reta: ')
            
            while True:
                try:
                    x1, y1 = map(float, input('Digite as coordenadas do ponto 1 (x y): ').split())
                    x2, y2 = map(float, input('Digite as coordenadas do ponto 2 (x y): ').split())
                    
                    if x1>=0 and x2>=0 and y1>=0 and y2>=0:
                        ponto1 = Ponto(nome, x1, y1)
                        ponto2 = Ponto(nome, x2, y2)
                        meu_segmento = SegmentoReta(nome, ponto1, ponto2)
                        self.dashboard.criar_forma(meu_segmento)
                        break
                    
                    else:
                        print('Os valores das coordenadas precisam ser maiores que 0')
                        saida = input('Deseja continuar criando o segmento de reta? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break
                    
                except:
                    print('Parâmetros inválidos para o segmento de reta.')
                    saida = input('Deseja continuar criando o segmento de reta? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break
                
        elif verificacao == 3:
            
            print('Vamos criar o Círculo!')
            print('')
            nome = input('Escreva o nome do círculo: ')
            
            while True:
                
                try:
                    x, y = map(float, input('Escreva as coordenadas do centro (separadas por espaço): ').split())
                    raio = float(input('Escreva o raio do círculo: '))
                    
                    if x>=0 and y>=0 and raio >0:
                        meu_circulo = Circulo(nome, x, y, raio)
                        self.dashboard.criar_forma(meu_circulo)
                        break
                    
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0, e o raio precisa ser maior que 0')
                        saida = input('Deseja continuar criando o círculo? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break
                
                except:
                    print('Parâmetros inválidos para o círculo.')
                    saida = input('Deseja continuar criando o círculo? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break

        elif verificacao == 4:
            
            print('Vamos criar o Retângulo!')
            print('')
            nome = input('Escreva o nome do retângulo: ')
            
            while True:
                try:
                    x, y = map(float, input('Escreva as coordenadas do canto inferior esquerdo (separadas por espaço): ').split())
                    altura = float(input('Escreva a altura do retângulo: '))
                    comprimento = float(input('Escreva o comprimento do retângulo: '))
                    
                    if x >=0 and y >=0 and altura >0 and comprimento>0:
                        meu_retangulo = Retangulo(nome, x, y, altura, comprimento)
                        self.dashboard.criar_forma(meu_retangulo)
                        break
                    
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0; a altura e o comprimento precisam ser maiores que 0')
                        saida = input('Deseja continuar criando o retângulo? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break        
                
                except:
                    print('Parâmetros inválidos para o retângulo.')
                    saida = input('Deseja continuar criando o retângulo? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break

        elif verificacao == 5:
            
            print('Vamos criar o Quadrado!')
            print('')
            nome = input('Escreva o nome do quadrado: ')
            
            while True:
                
                try:
                    x, y = map(float, input('Escreva as coordenadas do canto inferior esquerdo (separadas por espaço): ').split())
                    lado = float(input('Escreva o tamanho do lado do quadrado: '))
                    
                    if y>=0 and y>=0 and lado>0:
                        meu_quadrado = Quadrado(nome, x, y, lado)
                        self.dashboard.criar_forma(meu_quadrado)
                        break
                    
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0 e os lados precisam ser maiores que 0')
                        saida = input('Deseja continuar criando o quadrado? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break 
                
                except:
                    print('Parâmetros inválidos para o quadrado.')
                    saida = input('Deseja continuar criando o quadrado? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break

        elif verificacao == 6:
            
            print('Vamos criar o Triângulo!')
            print('')
            nome = input('Escreva o nome do triângulo: ')
            
            while True:
                
                try:
                    x1, y1 = map(float, input('Escreva as coordenadas do ponto 1 (separadas por espaço): ').split())
                    x2, y2 = map(float, input('Escreva as coordenadas do ponto 2 (separadas por espaço): ').split())
                    x3, y3 = map(float, input('Escreva as coordenadas do ponto 3 (separadas por espaço): ').split())
                    
                    if x1>=0 and x2>=0 and x1>=0 and y1>=0 and y1>=0 and y2>=0 and y3>=0:
                        ponto1 = Ponto(nome + "_1", x1, y1)
                        ponto2 = Ponto(nome + "_2", x2, y2)
                        ponto3 = Ponto(nome + "_3", x3, y3)
                        meu_triangulo = Triangulo(nome, ponto1, ponto2, ponto3)
                        self.dashboard.criar_forma(meu_triangulo)
                        break
                    
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar criando o triângulo? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break 
                        
                
                except:
                    print('Parâmetros inválidos para os pontos do triângulo.')
                    saida = input('Deseja continuar criando o triângulo? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break

        elif verificacao == 7:
            
            print('Vamos criar o Triângulo retângulo!')
            print('')
            nome = input('Escreva o nome do triângulo retângulo: ')
            
            while True:
                try:
                    x1, y1 = map(float, input('Escreva as coordenadas do ponto 1 (separadas por espaço): ').split())
                    x2, y2 = map(float, input('Escreva as coordenadas do ponto 2 (separadas por espaço): ').split())
                    x3, y3 = map(float, input('Escreva as coordenadas do ponto 3 (separadas por espaço): ').split())
                    
                    if x1>=0 and x2>=0 and x1>=0 and y1>=0 and y1>=0 and y2>=0 and y3>=0:
                        ponto1 = Ponto(nome + "_1", x1, y1)
                        ponto2 = Ponto(nome + "_2", x2, y2)
                        ponto3 = Ponto(nome + "_3", x3, y3)
                        meu_triangulo = TrianguloRetangulo(nome, ponto1, ponto2, ponto3)
                        self.dashboard.criar_forma(meu_triangulo)
                        break
                    
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar criando o triângulo retãngulo? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break 
                        
                
                except:
                    print('Parâmetros inválidos para os pontos do triângulo retângulo.')
                    saida = input('Deseja continuar criando o triânguloretângulo? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break
        
    def remover_formas(self):
        print('A seguintes formas estão cadastradas:')
        self.dashboard.listar_formas()
        
        while True:
            try:
                nome_forma = input('Você deseja remover qual forma? (Escreva o nome antes dos dois pontos) ')
                self.dashboard.remover_forma(nome_forma)
                break
                
            except:
                print('Nome inválido')
                saida = input('Deseja tentar novamente? (s/n): ').lower()
                print('')
                if saida[0] == 'n':
                    break
                
    def listar_formas(self):
        print('Formas cadastradas:')
        self.dashboard.listar_formas()
        
    def ponto_contido(self):   
        continuar = True
        print("""Escolha entre as seguintes opções:
    1. Usar um ponto já existente
    2. Usar um ponto novo
OBS: O novo ponto existirá apenas para a comparação da intersecção""")
        condicao_ponto = int(input('Escreva a opção escolhida:'))
        print('')   
        
        while True:
            if condicao_ponto == 1:
                print('Os Pontos cadastrados são:')
                self.dashboard.listar_formas_classe('ponto')
                print('')
                
                nome_ponto = input('Escreva o nome do ponto desejado: ')
                
                try:
                    ponto_comparacao = self.dashboard._objetos[nome_ponto]
                    break
                except:
                    print('Parãmetro do nome inválido')
                    saida = input('Deseja tentar novamente? (s/n): ').lower()
                    if saida[0] == 'n':
                        continuar = False
                        break
                    
            elif condicao_ponto == 2:
                try:
                    x, y = map(float, input('Escreva as coordenadas do ponto (separadas por espaço): ').split())
                    if x>=0 and y >= 0:
                        ponto_comparacao = Ponto('Apenas pra comparacao', x , y)
                        break
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar? (s/n): ').lower()
                        if saida[0] == 'n':
                            cotinuar = False
                            break
                
                except:
                    print('Parâmetros inválidos.')
                    saida = input('Deseja continuar? (s/n): ')
                    if saida[0] == 'n':
                        continuar = False
                        break
                
            else:
                print('O número deve ser 1 ou 2')
                saida = input('Deseja continuar? (s/n): ').lower()
                if saida[0] == 'n':
                    continuar = False
                    break
        if continuar:       
            print("""Você quer ver se ele está dentro do domínio de:
    1. Um retângulo já existente
    2. Um retângulo novo
    OBS: As formas criadas por aqui serão apenas para comparação, não para armazenamento""")
            
            condicao_forma = int(input('Escreva a opção escolhida: '))
            while True:
                try:        
                    if condicao_forma == 1:
                        while True:
                            print('Os retângulos cadastrados são:')
                            self.dashboard.listar_formas_classe('retangulo')
                            nome_forma = input('Escreva o nome do quadrado desejado (o nome antes dos dois pontos): ')
                            
                            try:
                                forma_comparada = self.dashboard._objetos[nome_forma]
                                break
                            
                            except:
                                print('Parãmetro do nome inválido')
                                saida = input('Deseja continuar? (s/n): ')
                                if saida[0] == 'n':
                                    continuar = False
                                    break
                        
                    elif condicao_forma == 2:
                        while True:
                            try:
                                x, y = map(float, input('Escreva as coordenadas do canto inferior esquerdo (separadas por espaço): ').split())
                                altura = float(input('Escreva a altura do retângulo: '))
                                comprimento = float(input('Escreva o comprimento do retângulo: '))
                                
                                if x >=0 and y >=0 and altura >0 and comprimento>0:
                                    forma_comparada = Retangulo('', x, y, altura, comprimento)
                                    break
                                
                                else:
                                    print('As coordenadas precisam ser maiores ou iguais a 0; a altura e o comprimento precisam ser maiores que 0')
                                    saida = input('Deseja continuar criando o retângulo? (s/n): ').lower()
                                    print('\n')
                                    if saida[0] == 'n':
                                        continuar = False
                                        break        
                            
                            except:
                                print('Parâmetros inválidos para o retângulo.')
                                saida = input('Deseja continuar criando o retângulo? (s/n): ').lower()
                                print('\n')
                                if saida[0] == 'n':
                                    continuar = False
                                    break
            
                    else:
                        print('Parâmtro inválido. Escreva 1 ou 2.')
                        saida = input('Deseja continuar? (s/n): ').lower()
                        if saida[0] == 'n':
                            continuar = False
                            break
                    
                except:
                    print('Parâmetros inválidos.')
                    saida = input('Deseja continuar? (s/n)').lower()
                    if saida[0] == 'n':
                        continuar = False
                        break
            
        if cotinuar:
            x_max = forma_comparada.get_Ponto_x() + forma_comparada.get_comprimento()
            y_max = forma_comparada.get_Ponto_y() + forma_comparada.get_altura
                
            if ponto_comparacao.get_x() >= x and ponto_comparacao.get_x()<= x_max and ponto_comparacao.get_y()>=y_max and ponto_comparacao.get_y() <= y_max:
                print('Ele está contido')
                print('')
            else:
                print('Ele não está contido')
                print('')
                
            
            
            
    def distancia_ponto_origem(self):

        while True:
            print("""Escolha entre as seguintes opções:
    1. Usar um ponto já existente
    2. Usar um ponto novo
OBS: O novo ponto existirá apenas para a comparação da distância""")
            condicao_ponto = int(input('Escreva a opção escolhida:'))
            print('')
            show_saida = True
            
            if condicao_ponto == 1:
                print('Os Pontos cadastrados são:')
                self.dashboard.listar_formas_classe('ponto')
                nome_ponto = input('Escreva o nome do ponto desejado: ')
                
                try:    
                    ponto_comparacao = self.dashboard._objetos[nome_ponto]
                    break
                
                except:
                    print('Parâmetro do nome inválido.')
                    saida = input('Deseja continuar? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break
                    print('')
                
                    
            elif condicao_ponto == 2:
                try:
                    x, y = map(float, input('Escreva as coordenadas do ponto (separadas por espaço): ').split())
                    if x>=0 and y >= 0:
                        ponto_comparacao = Ponto('Apenas pra comparacao', x , y)
                        break
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar? (s/n): ')
                        print('') 
                        if saida[0] == 'n':
                            break
                
                except:
                    print('Parâmetros inválidos.')
                    saida = input('Deseja continuar? (s/n): ')
                    print('')
                    if saida[0] == 'n':
                        break
                    
            else:
                print('O número deve ser 1 ou 2')
                saida = input('Deseja continuar criando o Ponto? (s/n): ').lower()
                print('')
                if saida[0] == 'n':
                    show_saida = False
                    break
                
        if show_saida:      
            print(f'A distância da origem até o Ponto fornecido é igual a {ponto_comparacao.distancia_origem():.2f}')
            print('')
            
    def distancia_entre_pontos(self):
## primeiro ponto  
        while True:
            print("""Escolha entre as seguintes opções para o primeiro Ponto:
    1. Usar um ponto já existente
    2. Usar um ponto novo
OBS: O novo ponto existirá apenas para a comparação da distância""")
            condicao_ponto = int(input('Escreva a opção escolhida:'))
            print('')
            
            show_saida = True
            
            if condicao_ponto == 1:
                print('Os Pontos cadastrados são:')
                self.dashboard.listar_formas_classe('ponto')
                nome_ponto = input('Escreva o nome do ponto desejado: ')
                
                try:    
                    ponto_1 = self.dashboard._objetos[nome_ponto]
                    break
                except:
                    print('Parâmetro do nome inválido.')
                    saida = input('Deseja continuar? (s/n): ').lower()
                    print('')
                    if saida[0] == 'n':
                        break
                    print('')
                 
            elif condicao_ponto == 2:
                try:
                    x, y = map(float, input('Escreva as coordenadas do ponto (separadas por espaço): ').split())
                    if x>=0 and y >= 0:
                        ponto_1 = Ponto('Apenas pra comparacao', x , y)
                        break
                    else:
                        print('As coordenadas precisam ser maiores ou iguais a 0')
                        saida = input('Deseja continuar? (s/n): ').lower()
                        print('')
                        if saida[0] == 'n':
                            break
                except:
                    print('Parâmetros inválidos.')
                    saida = input('Deseja continuar? (s/n): ')
                    print('')
                    if saida[0] == 'n':
                        break
                
            else:
                print('O número deve ser 1 ou 2')
                saida = input('Deseja continuar criando o Ponto 1? (s/n): ').lower()
                print('')
                if saida[0] == 'n':
                    show_saida = False
                    break
        
        if show_saida:   
            while True:
                print("""Escolha entre as seguintes opções para o ponto 2:
        1. Usar um ponto já existente
        2. Usar um ponto novo
    OBS: O novo ponto existirá apenas para a comparação da distância""")
                condicao_ponto = int(input('Escreva a opção escolhida:'))
                print('')
                
                if condicao_ponto == 1:
                    print('Os Pontos cadastrados são:\n')
                    self.dashboard.listar_formas_classe('ponto')
                    nome_ponto = input('Escreva o nome do ponto desejado: ')
                    
                    try:    
                        ponto_2 = self.dashboard._objetos[nome_ponto]
                        break
                    
                    except:
                        print('Parâmetro do nome inválido.')
                        saida = input('Deseja continuar? (s/n): ').lower()
                        if saida[0] == 'n':
                            break
                        print('')
                    
                        
                elif condicao_ponto == 2:
                    try:
                        x, y = map(float, input('Escreva as coordenadas do ponto (separadas por espaço): ').split())
                        if x>=0 and y >= 0:
                            ponto_2 = Ponto('Apenas pra comparacao', x , y)
                            break
                        else:
                            print('As coordenadas precisam ser maiores ou iguais a 0')
                            saida = input('Deseja continuar? (s/n): ')
                            if saida[0] == 'n':
                                break
                    
                    except:
                        print('Parâmetros inválidos.')
                        saida = input('Deseja continuar? (s/n): ')
                        print('')
                        if saida[0] == 'n':
                            break
                        
                else:
                    print('O número deve ser 1 ou 2')
                    saida = input('Deseja continuar criando o Ponto? (s/n): ').lower()
                    if saida[0] == 'n':
                        show_saida = False
                        break
                    
        if show_saida:
            reta_qualquer = SegmentoReta('', ponto_1,ponto_2)
            distancia = reta_qualquer.tamanho_reta()
            print(f'A distancia entre os dois pontos é igual a {distancia}')
            print('')
                    
    
    def show_area(self):
        while True:
            print('Esses são as formas disponíveis para mostrar área:')
            self.dashboard.listar_formas()
            nome = input('Escreva o nome da forma que você deseja obter a área: ')
            try:
                minha_forma = self.dashboard._objetos[nome]
                print(f'A area da forma {nome} é igual a {minha_forma.area()}')
                print('')
                break
            
            except:
                print('Parâmetro inválido')
                saida = input('Deseja continuar escolhendo? (s/n): ')
                print('')
                if saida[0] == 'n':
                    break

        
        
        
    def run(self):
        while True:
            try:
                print("""Escolha uma das seguintes opções:
    1. Criar uma forma geométrica
    2. Remover uma forma geométrica
    3. Imprimir forma gemétrica
    4. Verificar se o ponto está contido no retângulo
    5. Distância do Ponto até a Origem
    6. Distância entre dois Pontos
    7. Mostrar a área
    8. Sair""")
                
                saida = int(input('Escreva a opção escolhida: '))
                print('')
                
                if saida == 1:
                    self.criacao_formas()
                    
                elif saida == 2:
                    self.remover_formas()
                
                elif saida == 3:
                    self.listar_formas()
                    
                elif saida == 4:
                    self.ponto_contido()
                
                elif saida == 5:
                    self.distancia_ponto_origem()
                
                elif saida == 6:
                    self.distancia_entre_pontos()
                    
                elif saida == 7:
                    self.show_area()
                
                elif saida == 8:
                    print('Saindo do programa')
                    break
                else:
                    print('Opção inválida! Escolha um número de 1 a 8.')
                
            except:
                print('Ocorreu algum erro, escreva apenas um número, referente às opções.')
                

