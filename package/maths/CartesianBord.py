from package.maths.encapsulamento import Ponto, SegmentoReta, Circulo, Retangulo, Quadrado, Triangulo, TrianguloRetangulo

class CartesianBord:
    
    def __init__(self):
        self._objetos = {}
        self._contador = 0
        
    def criar_forma(self, forma):
        try:
            nome = forma._nome + str(self._contador)
            self._objetos[nome] = forma
            self._contador += 1
            print(f'A forma {forma._nome} foi criada com sucesso')
        except Exception as e:
            print(f'Ocorreu algum erro na criação dessa forma: {e}')
    
    def remover_forma(self, nome):
        try:
            if nome in self._objetos:
                del self._objetos[nome]
                print(f'A forma com nome {nome} foi removida com sucesso.')
            else:
                print(f'Forma com nome {nome} não encontrada.')
        except:
            print(f'Ocorreu algum erro na remoção da forma:')
    
    def listar_formas(self):
        if not self._objetos:
            print('Nenhuma forma cadastrada.')
        else:
            print('Formas cadastradas:')
            for nome, forma in self._objetos.items():
                print(f'{nome}: {forma.get_nome()}')

    def mostrar_detalhes(self, nome):
        try:
            if nome in self._objetos:
                forma = self._objetos[nome]
                forma.model()
            else:
                print(f'Forma com nome {nome} não encontrada.')
        except:
            print(f'Ocorreu algum erro ao mostrar detalhes da forma')