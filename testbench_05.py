from package.maths.encapsulamento import Quadrado

def quadrado_workspace():
    
    while True:    
        try: 
            nome = input('Insira o nome do quadrado:\n')
            x, y = map(int, input('Insira os valores inteiros e maiores que 0 para x e y do ponto inicial, separados por espaço:\n').split())
            lado = float(input('Insira o valor do lado (maior que 0):\n'))
            
            if x >= 0 and y >= 0 and lado > 0:
                quadrado = Quadrado(nome, x, y, lado)
                break
            else:
                print('x, y precisam ser maiores que 0 e o lado deve ser maior que 0')
                
        except:
            print('Parâmetro inválido para o ponto inicial ou lado')
    
    quadrado.model()
    
    validade = True
    
    if nome != quadrado.get_nome():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x != quadrado.get_Ponto_x() or y != quadrado.get_Ponto_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif lado != quadrado.get_lado():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try:
                novo_x, novo_y = map(float, input('Escreva novos valores para x e y do ponto inicial, separados por espaço:\n').split())
                novo_lado = float(input('Escreva um novo valor para o lado (maior que 0):\n'))
                
                if novo_x >= 0 and novo_y >= 0 and novo_lado > 0:
                    quadrado.set_x(novo_x)
                    quadrado.set_y(novo_y)
                    quadrado.set_lado(novo_lado)
                    quadrado.model()
                    break
                else: 
                    print('x e y precisam ser maiores que 0 e o lado deve ser maior que 0')
                    
            except:
                print('Parâmetro inválido para o ponto inicial ou lado')

        if novo_x != quadrado.get_Ponto_x() or novo_y != quadrado.get_Ponto_y():
            validade = False
            print('Deu problema no setter')
            
        elif novo_lado != quadrado.get_lado():
            validade = False
            print('Deu problema no setter')
    
    if validade:
        print('Deu tudo certo na criação do objeto quadrado')

if __name__ == "__main__":
    print('O workspace do Quadrado foi invocado\n')
    quadrado_workspace()
