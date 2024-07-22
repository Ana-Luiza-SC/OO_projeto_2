# testbench para o triangulo retangulo
from package.maths.encapsulamento import TrianguloRetangulo, Ponto

def triangulo_retangulo_workspace():
    while True:
        try:
            print('Recomendo ultilizar as coordenadas: (0,0); (0,3); (4,0)')
            x1, y1 = map(float, input('Insira as coordenadas do ponto 1 (x y), separadas por espaço:\n').split())
            x2, y2 = map(float, input('Insira as coordenadas do ponto 2 (x y), separadas por espaço:\n').split())
            x3, y3 = map(float, input('Insira as coordenadas do ponto 3 (x y), separadas por espaço:\n').split())

            if x1 >=0 and x2 >=0 and x3 >=0 and y1>=0 and y2>0 and y3>=0:
                ponto1 = Ponto("Ponto 1", x1, y1)
                ponto2 = Ponto("Ponto 2", x2, y2)
                ponto3 = Ponto("Ponto 3", x3, y3)
                meu_triangulo_retangulo = TrianguloRetangulo("Meu Triângulo Retângulo", ponto1, ponto2, ponto3)
                break
            else:
                print('O valor não pode ser negativo') 
        except:
            print('Coordenadas inválidas. Insira números inteiros.')

    print(f'O triângulo com pontos ({meu_triangulo_retangulo._ponto1.get_x()}, {meu_triangulo_retangulo._ponto1.get_y()}), ({meu_triangulo_retangulo._ponto2.get_x()}, {meu_triangulo_retangulo._ponto2.get_y()}), ({meu_triangulo_retangulo._ponto3.get_x()}, {meu_triangulo_retangulo._ponto3.get_y()}) foi criado com sucesso.')

         
    if (x1 != meu_triangulo_retangulo._ponto1.get_x() or y1 != meu_triangulo_retangulo._ponto1.get_y() or
        x2 != meu_triangulo_retangulo._ponto2.get_x() or y2 != meu_triangulo_retangulo._ponto2.get_y() or
        x3 != meu_triangulo_retangulo._ponto3.get_x() or y3 != meu_triangulo_retangulo._ponto3.get_y()):
        print('Houve um erro na criação do objeto triângulo.')
            
    if meu_triangulo_retangulo.is_retangulo():
        print("Os pontos fornecidos formam um triângulo retângulo.")
        print(f'A area do meu triângulo retangulo é igual a {meu_triangulo_retangulo.area():.2f}')
        print(f'O perímetro é igual a {meu_triangulo_retangulo.perimetro():.0f}')
    else:
        print("Os pontos fornecidos não formam um triângulo retângulo.")



if __name__ == "__main__":
    triangulo_retangulo_workspace()
