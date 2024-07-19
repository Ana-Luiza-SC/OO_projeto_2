# testbench para o triangulo retangulo
from package.maths.encapsulamento import TrianguloRetangulo, Ponto

def triangulo_retangulo_workspace():
    while True:
        try:
            print('sugetsão de coordenadas para a criação de um triângulo retângulo: (0,0), (0,4), (3,0)')
            x1, y1 = map(int, input('Insira as coordenadas do ponto 1 (x y), separadas por espaço:\n').split())
            x2, y2 = map(int, input('Insira as coordenadas do ponto 2 (x y), separadas por espaço:\n').split())
            x3, y3 = map(int, input('Insira as coordenadas do ponto 3 (x y), separadas por espaço:\n').split())
            
            if x1 >=0 and x2 >=0 and x3 >=0 and y1>=0 and y2>0 and y3>=0:
                ponto1 = Ponto("Ponto 1", "Preto", x1, y1)
                ponto2 = Ponto("Ponto 2", "Preto", x2, y2)
                ponto3 = Ponto("Ponto 3", "Preto", x3, y3)
                meu_triangulo_retangulo = TrianguloRetangulo("Meu Triângulo Retângulo", "Azul", ponto1, ponto2, ponto3)
                break
            else: 
                print('Os números precisam ser maiores ou iguais a zero')
            
        except:
            print('Coordenadas inválidas. Insira números inteiros.')
      
    validade = True
          
    if ponto1 != meu_triangulo_retangulo.getPonto1():
        validade = False
        
    if ponto2 != meu_triangulo_retangulo.getPonto2():
        validade = False
        
    if ponto3 != meu_triangulo_retangulo.getPonto3():
        validade = False
        
    if validade == True:
        print('O triângulofoi criado com sucesso.')
        
        if meu_triangulo_retangulo.is_retangulo():
            print("Os pontos fornecidos formam um triângulo retângulo.")
            print(f'A area do meu triângulo retangulo é igual a {meu_triangulo_retangulo.area():.2f}')
            print(f'O perímetro é igual a {meu_triangulo_retangulo.perimetro():.0f}')
        else:
            print("Os pontos fornecidos não formam um triângulo retângulo.")



if __name__ == "__main__":
    triangulo_retangulo_workspace()
