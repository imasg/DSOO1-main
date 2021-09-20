from MVC.entidade.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, id_cliente, cpf, nome, data_nascimento, fone, endereco):
        super().__init__(cpf, nome, data_nascimento, fone, endereco)
        self.__produtos = []
        self.__id_cliente = id_cliente
        self.idss = 1

    @property
    def id_cliente(self):
        return self.__id_cliente


    def add_produtudo(self, produto):
        self.__produtos.append(produto)