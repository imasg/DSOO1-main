import PySimpleGUI as sg

class TelaGeral:

    def __init__(self):
        pass

    def abrir_tela(self, lista_clientes):
        self.lista_clientes = lista_clientes
        lista = self.get_lista()


        sg.theme('Dark Brown')

        layout = [[sg.Text('Bem vindo(a)!!!')],
                  [sg.Text('Selecione um cliente para fazer as operações abaixo!!!')],
                  [sg.Listbox(values=lista, size=(20, 12), key='-LIST-', enable_events=True)],
                  [sg.Button('Sair')],
                  [sg.Button('Criar Cliente')],
                  [sg.Button('Excluir Cliente')],
                  [sg.Button('Gerenciar Cliente Selecionado')]]

        self.window = sg.Window('Tela Principal', layout)

        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Sair'):
                self.fechar_tela()
                break
            else:
                if event == '-LIST-':
                    self.cliente = self.get_cliente(values['-LIST-'][0])

                elif event == 'Criar Cliente':
                    layout1 = [
                        [sg.Text('Tela de Cadastro')],
                        [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                        [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                        [sg.Text('Nascimento', size=(15, 1)), sg.InputText()],
                        [sg.Text('Fone', size=(15, 1)), sg.InputText()],
                        [sg.Text('Endereco', size=(15, 1)), sg.InputText()],
                        [sg.Button('Enviar')],
                        [sg.Button('Cancelar')]
                    ]
                    self.window1 = sg.Window('Tela 2', layout1)
                    while True:
                        event, values = self.window1.read()
                        if event in (sg.WIN_CLOSED, 'Cancelar'):
                            self.window1.close()
                            break
                        else:
                            from MVC.controle.controle_geral import ControleGeral
                            ControleGeral().add_cliente(values[0], values[1], values[2], values[3], values[4])
                            self.window1.close()
                            break


                elif event == 'Excluir Cliente':
                    pass

                elif event == 'Gerenciar Cliente Selecionado':
                    pass

    def fechar_tela(self):
        self.window.close()

    def get_lista(self):
        lista = []
        for i in self.lista_clientes:
            lista.append(f"{i.id_cliente} - {i.nome}")
        return lista

    def get_cliente(self, dado):
        id = int(dado.split()[0])
        for i in self.lista_clientes:
            if i.id_cliente == id:
                return i

    # def get_add_cliente(self, cpf, nome, nascimento, fone, endereco):
    #     from MVC.controle.controle_geral import ControleGeral
    #     ControleGeral().add_cliente(cpf, nome, nascimento, fone, endereco)

    def get_del_cliente(self):
        from MVC.controle.controle_geral import ControleGeral
        ControleGeral().del_cliente()