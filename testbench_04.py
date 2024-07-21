from package.maths.encapsulamento import Retangulo

def retangulo_workspace():
    
    while True:    
        try: 
            nome = input('Insira o nome do retângulo:\n')
            x, y = map(int, input('Insira os valores inteiros e maiores que 0 para x e y do ponto inicial, separados por espaço:\n').split())
            altura = float(input('Insira o valor da altura (maior que 0):\n'))
            comprimento = float(input('Insira o valor do comprimento (maior que 0):\n'))
            
            if x >= 0 and y >= 0 and altura > 0 and comprimento > 0:
                retangulo = Retangulo(nome, x, y, altura, comprimento)
                break
            else:
                print('x, y precisam ser maiores que 0 e altura/comprimento devem ser maiores que 0')
                
        except:
            print('Parâmetro inválido para o ponto inicial ou dimensões')
    
    retangulo.model()
    
    validade = True
    
    if nome != retangulo.get_nome():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x != retangulo.get_Ponto_x() or y != retangulo.get_Ponto_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif altura != retangulo.get_altura() or comprimento != retangulo.get_comprimento():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try:
                novo_x, novo_y = map(float, input('Escreva novos valores para x e y do ponto inicial, separados por espaço:\n').split())
                nova_altura = float(input('Escreva um novo valor para a altura (maior que 0):\n'))
                novo_comprimento = float(input('Escreva um novo valor para o comprimento (maior que 0):\n'))
                
                if novo_x >= 0 and novo_y >= 0 and nova_altura > 0 and novo_comprimento > 0:
                    retangulo.set_x(novo_x)
                    retangulo.set_y(novo_y)
                    retangulo.set_altura(nova_altura)
                    retangulo.set_comprimento(novo_comprimento)
                    retangulo.model()
                    break
                else: 
                    print('x e y precisam ser maiores que 0 e altura/comprimento devem ser maiores que 0')
                    
            except:
                print('Parâmetro inválido para o ponto inicial ou dimensões')

        if novo_x != retangulo.get_Ponto_x() or novo_y != retangulo.get_Ponto_y():
            validade = False
            print('Deu problema no setter')
            
        elif nova_altura != retangulo.get_altura():
            validade = False
            print('Deu problema no setter')
            
        elif novo_comprimento != retangulo.get_comprimento():
            validade = False
            print('Deu problema no setter')
    
    if validade:
        print('Deu tudo certo na criação do objeto retângulo')

if __name__ == "__main__":
    print('O workspace do Retângulo foi invocado\n')
    retangulo_workspace()
