from package.maths.encapsulamento import Ponto, SegmentoReta

def segmento_reta_workspace():
    
    while True:    
        try: 
            nome = input('Insira o nome do segmento de reta:\n')
            x1, y1 = map(int, input('Insira os valores inteiros e maiores que 0 para x1 e y1 do primeiro ponto, separados por espaço:\n').split())
            x2, y2 = map(int, input('Insira os valores inteiros e maiores que 0 para x2 e y2 do segundo ponto, separados por espaço:\n').split())
            
            if x1 >= 0 and y1 >= 0 and x2 >= 0 and y2 >= 0:
                ponto1 = Ponto(nome, x1, y1)
                ponto2 = Ponto(nome, x2, y2)
                reta = SegmentoReta(nome, ponto1, ponto2)
                break
            else:
                print('x1, y1, x2 e y2 precisam ser maiores que 0')
                
        except:
            print('Parâmetro inválido para os pontos')
    
    reta.model()
    
    validade = True
    
    if nome != reta.get_nome():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x1 != reta.get_ponto1_x() or y1 != reta.get_ponto1_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x2 != reta.get_ponto2_x() or y2 != reta.get_ponto2_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try:
                novo_x1, novo_y1 = map(float, input('Escreva novos valores para x1 e y1 separados por espaço:\n').split())
                novo_x2, novo_y2 = map(float, input('Escreva novos valores para x2 e y2 separados por espaço:\n').split())
                
                if novo_x1 >= 0 and novo_y1 >= 0 and novo_x2 >= 0 and novo_y2 >= 0:
                    reta.set_ponto1_x(novo_x1)
                    reta.set_ponto1_y(novo_y1)
                    reta.set_ponto2_x(novo_x2)
                    reta.set_ponto2_y(novo_y2)
                    reta.model()
                    break
                else: 
                    print('x1, y1, x2 e y2 precisam ser maiores que 0')
                    
            except:
                print('Parâmetro inválido para os pontos')

        if novo_x1 != reta.get_ponto1_x() or novo_y1 != reta.get_ponto1_y():
            validade = False
            print('Deu problema no setter')
            
        elif novo_x2 != reta.get_ponto2_x() or novo_y2 != reta.get_ponto2_y():
            validade = False
            print('Deu problema no setter')
    
    if validade:
        print('Deu tudo certo na criação do objeto segmento de reta')

if __name__ == "__main__":
    print('O workspace do Segmento de Reta foi invocado\n')
    segmento_reta_workspace()
