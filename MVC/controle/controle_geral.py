from MVC.entidade.cliente import Cliente
from MVC.limite.tela_geral import TelaGeral


class ControleGeral:

    def __init__(self):
        self.__clientes = []
        self.__tela_geral = TelaGeral()
        self.ids = 1

    def iniciar(self):
        self.__clientes.append(Cliente(1, 9808, 'Matheus', 12312, 1321312, 123123))
        a = self.__tela_geral.abrir_tela(self.__clientes)
        print(a.nome)

    def add_cliente(self, cpf, nome, data_nascimento, fone, endereco):
        self.__clientes.append(Cliente(self.ids, cpf, nome, data_nascimento, fone, endereco))
        self.ids += 1

    def del_cliente(self):
        x = input("Digite o CPF do cliente que deseja excluir: ")
        for i in range(len(self.__clientes)):
            if self.__clientes[i].cpf == x:
                self.__clientes.pop(i)
                print("Cliente Removido")
                break
            else:
                print("Cliente não encontrado")
