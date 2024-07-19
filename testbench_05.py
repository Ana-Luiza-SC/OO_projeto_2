#testbench do quadrado
from package.maths.encapsulamento import Quadrado

def quadrado_workspace():
    while True:
        try:
            lado = int(input('Insira um valor inteiro e maior que 0 para o lado do quadrado:\n'))

            if lado > 0:
                meu_quadrado = Quadrado(lado)
                break
            else:
                print('O lado precisa ser maior que 0.')
        except ValueError:
            print('Parâmetro inválido. Insira um número inteiro.')

    print(f'O quadrado com lado {meu_quadrado.get_altura()} foi criado com sucesso.')

    validade = True

    if lado != meu_quadrado.get_altura() or lado != meu_quadrado.get_comprimento() or lado != meu_quadrado.get_lado():
        validade = False
        print('Houve um erro na criação do objeto.')

    if validade:
        while True:
            try:
                novo_lado = int(input('Insira um novo valor para o lado:\n'))

                if novo_lado > 0:
                    meu_quadrado.set_altura(novo_lado)
                    meu_quadrado.set_comprimento(novo_lado)
                    break
                else:
                    print('O lado precisa ser maior que 0.')
            except ValueError:
                print('Parâmetro inválido. Insira um número inteiro.')

        print(f'O quadrado foi atualizado para lado {meu_quadrado.get_altura()}.')

        if novo_lado != meu_quadrado.get_altura() or novo_lado != meu_quadrado.get_comprimento():
            validade = False
            print('Houve um problema no setter.')

    if validade:
        print(f'A área do quadrado é {meu_quadrado.area():.2f}.')
        meu_quadrado.diagonal()
        print('Deu tudo certo na criação do objeto quadrado.')

if __name__ == "__main__":
    print('O workspace do Quadrado foi invocado.\n')
    quadrado_workspace()
else:
    print('Deu ruim.')
