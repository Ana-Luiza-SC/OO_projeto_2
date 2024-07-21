from package.maths.encapsulamento import Triangulo, Ponto

def triangulo_workspace():
    while True:
        try:
            x1, y1 = map(int, input('Insira as coordenadas do ponto 1 (x y), separadas por espaço:\n').split())
            x2, y2 = map(int, input('Insira as coordenadas do ponto 2 (x y), separadas por espaço:\n').split())
            x3, y3 = map(int, input('Insira as coordenadas do ponto 3 (x y), separadas por espaço:\n').split())

            if x1 >=0 and x2 >=0 and x3 >=0 and y1>=0 and y2>0 and y3>=0:
                ponto1 = Ponto("Ponto 1", "Preto", x1, y1)
                ponto2 = Ponto("Ponto 2", "Preto", x2, y2)
                ponto3 = Ponto("Ponto 3", "Preto", x3, y3)
                meu_triangulo = Triangulo("Meu Triângulo Retângulo", "Azul", ponto1, ponto2, ponto3)
                break
            else:
                print('O valor não pode ser negativo') 
        except:
            print('Coordenadas inválidas. Insira números inteiros.')

    print(f'O triângulo com pontos ({meu_triangulo.getPonto1().get_x()}, {meu_triangulo.getPonto1().get_y()}), ({meu_triangulo.getPonto2().get_x()}, {meu_triangulo.getPonto2().get_y()}), ({meu_triangulo.getPonto3().get_x()}, {meu_triangulo.getPonto3().get_y()}) foi criado com sucesso.')

    validade = True

    if (x1 != meu_triangulo.getPonto1().get_x() or y1 != meu_triangulo.getPonto1().get_y() or
        x2 != meu_triangulo.getPonto2().get_x() or y2 != meu_triangulo.getPonto2().get_y() or
        x3 != meu_triangulo.getPonto3().get_x() or y3 != meu_triangulo.getPonto3().get_y()):
        validade = False
        print('Houve um erro na criação do objeto triângulo.')

    if validade:
        while True:
            try:
                novo_x1, novo_y1 = map(int, input('Insira novas coordenadas para o ponto 1 (x y), separadas por espaço:\n').split())
                novo_x2, novo_y2 = map(int, input('Insira novas coordenadas para o ponto 2 (x y), separadas por espaço:\n').split())
                novo_x3, novo_y3 = map(int, input('Insira novas coordenadas para o ponto 3 (x y), separadas por espaço:\n').split())

                meu_triangulo.getPonto1().set_x(novo_x1)
                meu_triangulo.getPonto1().set_y(novo_y1)
                meu_triangulo.getPonto2().set_x(novo_x2)
                meu_triangulo.getPonto2().set_y(novo_y2)
                meu_triangulo.getPonto3().set_x(novo_x3)
                meu_triangulo.getPonto3().set_y(novo_y3)

                print(f'O triângulo foi atualizado para pontos ({meu_triangulo.getPonto1().get_x()}, {meu_triangulo.getPonto1().get_y()}), ({meu_triangulo.getPonto2().get_x()}, {meu_triangulo.getPonto2().get_y()}), ({meu_triangulo.getPonto3().get_x()}, {meu_triangulo.getPonto3().get_y()}).')

                if (novo_x1 != meu_triangulo.getPonto1().get_x() or novo_y1 != meu_triangulo.getPonto1().get_y() or
                    novo_x2 != meu_triangulo.getPonto2().get_x() or novo_y2 != meu_triangulo.getPonto2().get_y() or
                    novo_x3 != meu_triangulo.getPonto3().get_x() or novo_y3 != meu_triangulo.getPonto3().get_y()):
                    validade = False
                    print('Houve um problema no setter.')

                break
            except:
                print('Coordenadas inválidas. Insira números inteiros.')

    if validade:
        print(f'O perímetro do triângulo é {meu_triangulo.perimetro():.2f}.')
        print('Deu tudo certo na criação do objeto triângulo.')

if __name__ == "__main__":
    print('O workspace do Triângulo foi invocado.\n')
    triangulo_workspace()
else:
    print('Erro ao invocar o workspace do Triângulo.')