from package.maths.interface import Menu


def workspace():
    menu = Menu()
    menu.run()
    
    
if __name__ == '__main__':
    print('O arquivo foi invocado como main\n')
    workspace()
    
else:
    print('Deu algum erro na criação do workspace')