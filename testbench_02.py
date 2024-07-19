#vou usar agregação entre o ponto e o segmento de reta
#testbench do segmneto de reta
from package.maths.encapsulamento import Ponto, SegmentoReta

def segmento_reta_workspace():
    
    while True:    
        try: 
            nome, cor = input('Insira o nome e cor do segmento de reta, separados por espaço:\n').split()
            break
        
        except:
            print('Parâmetro inválido para cor ou nome')
    
    while True:
        try:
            x1, y1 = map(int, input('Insira os valores inteiros e maiores que 0 para x1 e y1, separados por espaço:\n').split())
            x2, y2 = map(int, input('Insira os valores inteiros e maiores que 0 para x2 e y2, separados por espaço:\n').split())
            
            if (x1 >= 0 and y1 >= 0) and (x2 >= 0 and y2 >= 0):
                ponto1 = Ponto(nome, cor, x1, y1)
                ponto2 = Ponto(nome, cor, x2, y2)
                break
            
            else: 
                print('x1 e y1 precisam ser maiores que 0')
        except:
            print('Parâmetro inválido, as coordenadas do ponto precisam ser números inteiros')
            
    meu_segmento = SegmentoReta(nome, cor, ponto1, ponto2)
    meu_segmento.model()
    
    validade = True
    
    if nome != meu_segmento.get_nome():
        validade = False
        print('Houve erro na criação do objeto')
        
    if cor != meu_segmento.get_cor():
        validade = False
        print('Houve erro na criação do objeto')
        
    if x1 != meu_segmento.get_ponto1_x() or y1 != meu_segmento.get_ponto1_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    if x2 != meu_segmento.get_ponto2_x() or y2 != meu_segmento.get_ponto2_y():
        validade = False
        print('Houve erro na criação do objeto')
        
    if validade == True:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try: 
                novo_x1, novo_y1 = map(int, input('Escreva novos valores para x1 e y1 separados por espaço:\n').split())
                novo_x2, novo_y2 = map(int, input('Escreva novos valores para x2 e y2 separados por espaço:\n').split())
                
                if (novo_x1 >= 0 and novo_y1 >= 0) and (novo_x2 >= 0 and novo_y2 >= 0):
                    meu_segmento.set_ponto1_x(novo_x1)
                    meu_segmento.set_ponto1_y(novo_y1)
                    meu_segmento.set_ponto2_x(novo_x2)
                    meu_segmento.set_ponto2_y(novo_y2)
                    break
                else:
                    print('Parâmetro inválido, as coordenadas do ponto precisam ser números inteiros')
                
            except:
                print('Parâmetro inválido, as coordenadas do ponto precisam ser números inteiros')
        
        meu_segmento.model()
        
        if novo_x1 != meu_segmento.get_ponto1_x():
            validade = False
            print('Deu problema no setter')
            
        if novo_y1 != meu_segmento.get_ponto1_y():
            validade = False
            print('Deu problema no setter')
            
        if novo_x2 != meu_segmento.get_ponto2_x():
            validade = False
            print('Deu problema no setter')
            
        if novo_y2 != meu_segmento.get_ponto2_y():
            validade = False
            print('Deu problema no setter')
    
    if validade == True:
        print(f'O tamanho da reta é igual a {meu_segmento.tamanho_reta():.2f} e sua inclinação é igual a {meu_segmento.calcular_inclinacao():.2f}')
        
        print('Deu tudo certo na criação do objeto segmento de reta e na associação fraca dos pontos com o segmento')
        
    
            

if __name__ == "__main__":
    print('O workspace do Segmento de Reta foi invocado\n\n') # quero pular duas linhas para deixar mais claro onde vai começar o workspace
    segmento_reta_workspace()
    
else:
    print('Deu ruim')
