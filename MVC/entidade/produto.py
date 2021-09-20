class Produto:

    def __init__(self, fabrincate, nome, ano):
        self.__fabricante = fabrincate
        self.__nome = nome
        self.__ano = ano

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabr):
        self.__fabricante = fabr

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nomee):
        self.__nome = nomee

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, anoo):
        self.__ano = anoo
