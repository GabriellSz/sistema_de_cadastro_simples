class Pessoa(object):
    def __init__(self):
        print("")
        self.nome_de_usuario = ""
        self.nome_completo = self.pegar_nome_completo()
        self.cidade = self.pegar_cidade()
        self.profissao = self.pegar_profissao()
        self.idade = self.pegar_idade()

    #   output methods
    def mostrar_dados(self):
        print(
        f"""
        ========================================
        Nome de Usuario: {self.nome_de_usuario} 
        ----------------------------------------
            Nome: {self.nome_completo.title()}
            cidade: {self.cidade.title()}
            Profissão: {self.profissao.title()}
            Idade: {self.idade}
        ========================================    
        """)

    # input methods
    def pegar_nome_completo(self):
        input_errado = True
        while input_errado:
            nome_completo = self.pegar_input_de_string("Nome Completo: ").upper()
            input_errado = self.tratar_input_de_string(nome_completo, 2, 50)            
        return nome_completo

    def pegar_cidade(self):
        input_errado = True
        while input_errado:
            cidade = self.pegar_input_de_string("Cidade: ").upper()
            input_errado = self.tratar_input_de_string(cidade, 3, 20)
        return cidade
                
    def pegar_profissao(self):
        input_errado = True
        while input_errado:
            profissao = self.pegar_input_de_string("Profissão: ").upper()
            input_errado = self.tratar_input_de_string(profissao, 3, 20)
        return profissao

    def pegar_idade(self):
        input_errado = True
        while input_errado:
            idade = self.pegar_input_de_inteiro("Idade: ")
            input_errado = self.tratar_input_de_inteiro(idade, 18, 65)
        return idade

    def pegar_input_de_string(self, mensagem):
        while True:
            try:
                entrada = input(mensagem).strip()
                return entrada
            except ValueError:
                print("\n Digite um valor válido por favor \n")
                continue

    def pegar_input_de_inteiro(self, mensagem):
        while True:
            try:
                entrada = int(input(mensagem).strip())
                return entrada
            except ValueError:
                print("\n Digite um valor válido por favor \n")
                continue

    # error handling methods
    def tratar_input_de_string(self, entrada, tamanho_minimo, tamanho_maximo):
        if len(entrada) < tamanho_minimo:
            print(f"\n Você deve digitar pelo menos {tamanho_minimo} caracteres. \n")
            return True
        elif len(entrada) > tamanho_maximo:
            print(f"\n você deve digitar no maximo {tamanho_maximo} caracteres. \n")
            return True
        else:
            return False

    def tratar_input_de_inteiro(self, entrada, valor_minimo, valor_maximo):
        if int(entrada) < valor_minimo:
            print(f"\n Você deve inserir um valor maior que {valor_minimo}. \n")
            return True
        elif int(entrada) > valor_maximo:
            print(f"\n Você deve digitar um valor menor que {valor_maximo}. \n")
            return True
        else:
            return False

class Formulario(Pessoa):
    def __init__(self):
        print("Abrindo formulario para cadastros... \n")
        self.cadastrados = {}
        self.metodos_interaveis = {
            0: self.encerrar,
            1: self.cadastrar_cliente, 
            2: self.mostrar_clientes_cadastrados,
            3: self.procurar_dados_de_um_cliente,
            4: self.atualizar_dados_de_um_cliente,
            5: self.excluir_cliente_do_sistema
        }

    def iniciar_o_formulario(self):
        self.menu_de_opcoes()
                                  
    # output methods
    def mostrar_clientes_cadastrados(self):
        if len(self.cadastrados.keys()) > 0:
            for cliente in self.cadastrados:
                print(f"\n {cliente} - Nome de usuario: {(self.cadastrados[cliente].nome_de_usuario)}")
        else:
            print("\n Nenhum cliente cadastrado, tente cadastrar um novo \n")

    def encerrar(self):
        print("\n Encerrando Programa... \n")
        exit()
    
    # menu input methods
    def menu_de_opcoes(self):
        encerrar = False
        while encerrar == False:
            print(
            """
            [1] - Cadastrar Novo Cliente
            [2] - Ver Usuarios Cadastrados

            [3] - Procurar dados de um cliente
            [4] - Atualizar dados de um cliente
            [5] - Excluir cliente do sistema

            [0] - Sair
            """)
            input_errado = True
            while input_errado:
                escolha_do_usuario = self.pegar_input_de_inteiro(">: ")
                input_errado = self.tratar_input_de_inteiro(escolha_do_usuario, 0, len(self.metodos_interaveis.keys()))
            
            for opcao in self.metodos_interaveis.keys():
                if escolha_do_usuario == opcao:
                    self.metodos_interaveis[escolha_do_usuario]()
                    if escolha_do_usuario == 0:
                        encerrar = True

    def cadastrar_cliente(self):
        continuar = True
        while continuar:
            novo_cadastro = Pessoa()
            novo_cadastro.nome_de_usuario = self.pegar_nome_de_usuario()
            print("\n Cadastro Efetuado com sucesso \n")
            self.__cria_novo_cadastro(novo_cadastro)

            continuar = self.pergunta_se_vai_continuar("\n Deseja cadastrar mais algum cliente? [1] - sim  [2] - não")
 
    def procurar_dados_de_um_cliente(self):
        continuar = True
        while continuar:
            if len(self.cadastrados.keys()) > 0:
                input_errado = True
                while input_errado:
                    nome_usuario_para_pesquisa = self.pegar_input_de_string("Nome de usuario: ").upper()
                    input_errado = self.tratar_input_de_string(nome_usuario_para_pesquisa, 4, 20)
                
                for cliente in self.cadastrados.keys():
                    if nome_usuario_para_pesquisa in self.cadastrados[cliente].nome_de_usuario:
                        self.cadastrados[cliente].mostrar_dados()
                        return self.cadastrados[cliente]
                else:
                    print("Cliente não encontrado, tente outro nome de usuario.")
                        
                continuar = self.pergunta_se_vai_continuar("Deseja procurar por outro nome de usuario?  [1] - sim  [2] - não")
            else:
                print("\n Nenhum cliente cadastrado, tente cadastrar um novo \n")
                continuar = False

    def atualizar_dados_de_um_cliente(self):
        continuar = True
        while continuar:
            dados_do_cliente = self.procurar_dados_de_um_cliente()
            if len(self.cadastrados.keys()) > 0:
                nome_de_usuario_ = dados_do_cliente.nome_de_usuario
                atualizar = self.pergunta_se_vai_continuar("Atualizar dados do cliente? [1] - sim  [2] - não")

                if atualizar:
                    novos_dados_do_cliente = Pessoa()
                    dados_do_cliente.nome_completo, dados_do_cliente.cidade, dados_do_cliente.profissao, dados_do_cliente.idade = novos_dados_do_cliente.nome_completo, novos_dados_do_cliente.cidade, novos_dados_do_cliente.profissao, novos_dados_do_cliente.idade
                    dados_do_cliente.nome_de_usuario = nome_de_usuario_
                    print("Dados do cliente atualizado.")
                
                continuar = self.pergunta_se_vai_continuar("Deseja atualizar os dados de outro cliente? [1] - sim  [2] - não")
            else:
                continuar = False 

    def excluir_cliente_do_sistema(self):
        continuar = True
        while continuar:
            dados_do_cliente = self.procurar_dados_de_um_cliente()
            if len(self.cadastrados.keys()) > 0:
                nome_de_usuario_ = dados_do_cliente.nome_de_usuario
                excluir = self.pergunta_se_vai_continuar("Excluir cliente do sistema? [1] - sim  [2] - não")

                if excluir:
                    for cliente in self.cadastrados.keys():
                        if dados_do_cliente.nome_de_usuario in self.cadastrados[cliente].nome_de_usuario:
                            del(self.cadastrados[cliente])
                            print("")
                            break
                        else:
                            print("Cliente não encontrado, tente outro nome de usuario.")
                    print("\n Cliente Exluido do sistema. \n")
                
                continuar = self.pergunta_se_vai_continuar("Deseja excluir os dados de outro cliente? [1] - sim  [2] - não")
            else:
                continuar = False 
    
    # program input methods
    def pergunta_se_vai_continuar(self, mensagem):
        input_errado = True
        while input_errado:
            print(mensagem)
            escolha_usuario = self.pegar_input_de_inteiro(">: ")
            input_errado = self.tratar_input_de_inteiro(escolha_usuario, 1, 2)
        
        if escolha_usuario == 1:
            return True
        elif escolha_usuario == 2:
            return False   

    def pegar_nome_de_usuario(self):        
        while True:
            input_errado = True
            while input_errado:
                nome_de_usuario = self.pegar_input_de_string("Nome de Usuario: ").strip().upper()
                input_errado = self.tratar_input_de_string(nome_de_usuario, 4, 20)

            if " " in nome_de_usuario:
                print("O seu nome de usuario não deve conter espaços.")
                input_errado = True
            else:
                ja_tem_cadastro = self.__verifica_se_ja_tem_cadastro(nome_de_usuario)
                if ja_tem_cadastro:
                    print("Esse nome de usuario já está cadastrado, tente outro.")
                else:
                    break

        return nome_de_usuario

    # private and error handling methods
    def __verifica_se_ja_tem_cadastro(self, novo_nome_de_usuario):
        if len(self.cadastrados) > 0: 
            for cadastros in self.cadastrados:
                if novo_nome_de_usuario in self.cadastrados[cadastros].nome_de_usuario:
                    return True
                else:
                    return False
        else:
            return False

    def __cria_novo_cadastro(self, dados_da_pessoa):
        num_de_cadastro = (len(self.cadastrados))+1
        self.cadastrados[num_de_cadastro] = dados_da_pessoa

if __name__ == '__main__':
    formulario = Formulario()
    formulario.iniciar_o_formulario()
    
