# vou usar composição forte entre o ponto e o círculo
#testbench do circulo
from package.maths.encapsulamento import Circulo

def circulo_workspace():
    
    while True:    
        try: 
            forma, cor = input('Insira o nome da forma e cor do círculo, separados por espaço:\n').split()
            break
        
        except:
            print('Parâmetro inválido para cor ou nome')
    
    while True:
        try:
            x, y, raio = map(int, input('Insira os valores inteiros e maiores que 0 para x, y e raio, separados por espaço:\n').split())
            
            if (x >= 0 and y >= 0 and raio > 0):
                meu_circulo = Circulo(forma, cor, x, y, raio)
                break
            
            else: 
                print('x, y e raio precisam ser maiores que 0')
        except:
            print('Parâmetro inválido, as coordenadas e o raio precisam ser números inteiros')
    
    meu_circulo._centro.model()
    print(f'O círculo {meu_circulo._centro.get_forma()} de cor {meu_circulo._centro.get_cor()} e raio {meu_circulo.get_raio()} foi criado com sucesso.')
    print(f'Centro: ({meu_circulo.get_centro_x()}, {meu_circulo.get_centro_y()})')
    
    validade = True
    
    if forma != meu_circulo._centro.get_forma():
        validade = False
        print('Houve erro na criação do objeto')
        
    if cor != meu_circulo._centro.get_cor():
        validade = False
        print('Houve erro na criação do objeto')
        
    if x != meu_circulo.get_centro_x() or y != meu_circulo.get_centro_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    if raio != meu_circulo.get_raio():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade == True:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try: 
                novo_x, novo_y = map(int, input('Escreva novos valores para x e y separados por espaço:\n').split())
                novo_raio = int(input('Escreva um novo valor para o raio:\n'))
                
                if (novo_x >= 0 and novo_y >= 0 and novo_raio > 0):
                    meu_circulo.set_x(novo_x)
                    meu_circulo.set_y(novo_y)
                    meu_circulo.set_raio(novo_raio)
                    break
                else:
                    print('Parâmetro inválido, as coordenadas e o raio precisam ser números inteiros e maiores que 0')
                
            except:
                print('Parâmetro inválido, as coordenadas e o raio precisam ser números inteiros e maiores que 0')

        
        meu_circulo._centro.model()
        print(f'O círculo foi atualizado para centro ({meu_circulo.get_centro_x()}, {meu_circulo.get_centro_y()}) e raio {meu_circulo.get_raio()}')
        
        if novo_x != meu_circulo.get_centro_x():
            validade = False
            print('Deu problema no setter')
            
        if novo_y != meu_circulo.get_centro_y():
            validade = False
            print('Deu problema no setter')
            
        if novo_raio != meu_circulo.get_raio():
            validade = False
            print('Deu problema no setter')
    
    if validade == True:
        meu_circulo.model()
        print(f'A área do círculo é {meu_circulo.area():.2f}')
        meu_circulo.distancia_centro_origem()
        print('Deu tudo certo na criação do objeto círculo e na associação forte do ponto com o círculo')

if __name__ == "__main__":
    print('O workspace do Círculo foi invocado\n') 
    circulo_workspace()
    
else:
    print('Deu ruim')
