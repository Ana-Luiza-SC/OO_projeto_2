from package.maths.encapsulamento import Ponto, SegmentoReta, Circulo, Retangulo, Quadrado, Triangulo, TrianguloRetangulo

class CartesianBoard:
    
    def __init__(self):
        self._objetos = {}
        self._contador = 0
        
    def criar_forma(self, forma):
        
        try:
            nome = forma._nome + '_' + str(self._contador)
            self._objetos[nome] = forma
            self._contador += 1
            print(f'A forma {forma._nome} foi criada com sucesso\n')
            
        except:
            print(f'Ocorreu algum erro na criação dessa forma.')
    
    def remover_forma(self, nome):
        try:
            if nome in self._objetos:
                del self._objetos[nome]
                print(f'A forma com nome {nome} foi removida com sucesso.')
                
            else:
                print(f'Forma com nome {nome} não encontrada.')
                
        except:
            print(f'Ocorreu algum erro na remoção da forma.')
    
    def listar_formas(self):
        if not self._objetos:
            print('Nenhuma forma cadastrada.')
            
        else:
            for nome, forma in self._objetos.items():
                print(f'{nome}: {forma.get_nome()} da classe {forma.get_tipo()}')
        print('')
                
    def listar_formas_classe(self,tipo):
        if not self._objetos:
            print('Nenhuma forma cadastrada.')
            
        else:
            for nome, forma in self._objetos.items():
                if  forma.get_tipo() == 'ponto':
                     print(f'{nome}')

    def mostrar_detalhes(self, nome):
        try:
            if nome in self._objetos:
                forma = self._objetos[nome]
                forma.model()
                
            else:
                print(f'Forma com nome {nome} não encontrada.')
                
        except:
            print(f'Ocorreu algum erro ao mostrar detalhes da forma:') 
