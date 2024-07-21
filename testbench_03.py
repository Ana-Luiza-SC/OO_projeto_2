from package.maths.encapsulamento import Circulo

def circulo_workspace():
    
    while True:    
        try: 
            nome = input('Insira o nome do círculo:\n')
            x, y = map(int, input('Insira os valores inteiros e maiores que 0 para x e y do centro, separados por espaço:\n').split())
            raio = float(input('Insira o valor do raio (maior que 0):\n'))
            
            if x >= 0 and y >= 0 and raio > 0:
                circulo = Circulo(nome, x, y, raio)
                break
            else:
                print('x, y precisam ser maiores que 0 e o raio deve ser maior que 0')
                
        except:
            print('Parâmetro inválido para o centro ou raio')
    
    circulo.model()
    
    validade = True
    
    if nome != circulo.get_nome():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x != circulo.get_centro_x() or y != circulo.get_centro_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif raio != circulo.get_raio():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try:
                novo_x, novo_y = map(float, input('Escreva novos valores para x e y do centro, separados por espaço:\n').split())
                novo_raio = float(input('Escreva um novo valor para o raio (maior que 0):\n'))
                
                if novo_x >= 0 and novo_y >= 0 and novo_raio > 0:
                    circulo.set_x(novo_x)
                    circulo.set_y(novo_y)
                    circulo.set_raio(novo_raio)
                    circulo.model()
                    break
                else: 
                    print('x e y precisam ser maiores que 0 e o raio deve ser maior que 0')
                    
            except:
                print('Parâmetro inválido para o centro ou raio')

        if novo_x != circulo.get_centro_x() or novo_y != circulo.get_centro_y():
            validade = False
            print('Deu problema no setter')
            
        elif novo_raio != circulo.get_raio():
            validade = False
            print('Deu problema no setter')
    
    if validade:
        print('Deu tudo certo na criação do objeto círculo')

if __name__ == "__main__":
    print('O workspace do Círculo foi invocado\n')
    circulo_workspace()
