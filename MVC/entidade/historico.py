from MVC.entidade.ordem_de_servico import OrdemDeServico

class Historico:

    def __init__(self):
        self.__ordens_de_servicos = []

    def add_ordem(self, ordem):
        self.__ordens_de_servicos.append(ordem)

    def historico(self):
        return OrdemDeServico.add_ordem()

    def get_ordem(self):
        return self.__ordens_de_servicos


