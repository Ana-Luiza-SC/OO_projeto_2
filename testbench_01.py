#testbench do Ponto
# vou ultilizar uma associação fraca entre ponto e forma
from package.maths.encapsulamento import Ponto, Formas

def ponto_workspace():
    
    while True:    
        try: 
            nome = input('Insira o nome e cor, separados por espaço:\n')
            lados = 0 ## estou criando um ponto, não tem lado
            forma_1 = Formas(nome, lados)
            break
        
        except:
            print('Parãmetro inválido para cor ou nome')
    
    while True:
        try:
            x, y = map(int, input('Insira os valores inteiros e maiores que 0 para x e y, separados por espaço:\n').split())
            
            if x >=0 and y >=0:
                meu_ponto_1 = Ponto(forma_1, x, y)
                break
            
            else: 
                print('x e y precisam ser maiores que 0')
                
        except:
            print('Parametro inválido, x e y precisam ser números inteiros')
            
    forma_1.model()
    meu_ponto_1.model()
    
    validade = True #para verificar se foi criado certinho
    
    if nome != forma_1.get_nome() and meu_ponto_1.get_nome() != nome:
        validade = False
        print('Houve erro na criação do objeto')
        
    elif lados != forma_1.get_lados():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif x != meu_ponto_1.get_x():
        validade = False
        print('Houve erro na criação do objeto')
        
    elif y != meu_ponto_1.get_y():
        validade = False
        print('Houve erro na criação do objeto')
        
        
    if validade == True:
        print('Deu tudo certo na criação do objeto')
        
        while True:
            try:
                novo_x, novo_y = map(float, input('Escreva novos valores para x e y separados por espaço:\n').split())
                
                if novo_x >=0 and novo_y >=0:
                    meu_ponto_1.set_x(novo_x)
                    meu_ponto_1.set_y(novo_y)
                    meu_ponto_1.model()
                    break
                else: 
                    print('x e y precisam ser maiores que 0')
                    
            except:
                print('Parametro inválido, x e y precisam ser números inteiros')

        if novo_x != meu_ponto_1.get_x():
            validade = False
            print('Deu problema no setter')
            
        elif novo_y != meu_ponto_1.get_y():
            validade = False
            print('Deu problema no setter')
    
    if validade == True:
        print('Deu tudo certo na criação do objeto ponto e na associação fraca do mesmo com formas')
            


if __name__ == "__main__":
    print('O workspace do Ponto foi invocado\n') # quero pular duas linhas para deixar mais claro onde vai começar o workspace
    ponto_workspace()
    
else:
    print('Deu ruim')