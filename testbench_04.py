## testbench do retangulo
from package.maths.encapsulamento import Retangulo

def retangulo_workspace():
    while True:
        try:
            altura = int(input('Insira um valor inteiro e maior que 0 para a altura do retângulo:\n'))
            comprimento = int(input('Insira um valor inteiro e maior que 0 para o comprimento do retângulo:\n'))

            if altura > 0 and comprimento > 0:
                meu_retangulo = Retangulo(altura, comprimento)
                break
            else:
                print('Altura e comprimento precisam ser maiores que 0.')
        except ValueError:
            print('Parâmetro inválido. Insira um número inteiro.')

    print(f'O retângulo com altura {meu_retangulo.get_altura()} e comprimento {meu_retangulo.get_comprimento()} foi criado com sucesso.')

    validade = True

    if altura != meu_retangulo.get_altura():
        validade = False
        print('Houve um erro na criação do objeto.')

    if comprimento != meu_retangulo.get_comprimento():
        validade = False
        print('Houve um erro na criação do objeto.')

    if validade:
        while True:
            try:
                nova_altura = int(input('Insira um novo valor para a altura:\n'))
                novo_comprimento = int(input('Insira um novo valor para o comprimento:\n'))

                if nova_altura > 0 and novo_comprimento > 0:
                    meu_retangulo.set_altura(nova_altura)
                    meu_retangulo.set_comprimento(novo_comprimento)
                    break
                else:
                    print('Altura e comprimento precisam ser maiores que 0.')
            except ValueError:
                print('Parâmetro inválido. Insira um número inteiro.')

        print(f'O retângulo foi atualizado para altura {meu_retangulo.get_altura()} e comprimento {meu_retangulo.get_comprimento()}.')

        if nova_altura != meu_retangulo.get_altura():
            validade = False
            print('Houve um problema no setter.')

        if novo_comprimento != meu_retangulo.get_comprimento():
            validade = False
            print('Houve um problema no setter.')

    if validade:
        print(f'A área do retângulo é {meu_retangulo.area():.2f}.')
        meu_retangulo.diagonal()
        print('Deu tudo certo na criação do objeto retângulo.')

if __name__ == "__main__":
    print('O workspace do Retângulo foi invocado.\n')
    retangulo_workspace()
else:
    print('Deu ruim.')


