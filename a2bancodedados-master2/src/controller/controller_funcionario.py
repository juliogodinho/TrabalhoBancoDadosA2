from model.funcionario import Funcionario
from conexion.oracle_queries import OracleQueries

class Controller_funcionario:
    def __init__(self):
        pass
        
    def inserir_funcionario(self) -> Funcionario:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        opcao = 1
        while opcao == 1:
            # Solicita ao usuario o novo CPF
            cpf = input("CPF (Novo): ")

            if self.verifica_existencia_funcionario(oracle, cpf):
                # Solicita ao usuario o novo nome
                nome = input("Nome (Novo): ")
                # Insere e persiste o novo funcionario
                oracle.write(f"insert into funcionario values ('{cpf}', '{nome}')")
                # Recupera os dados do novo funcionario criado transformando em um DataFrame
                df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome from funcionario where cpf = '{cpf}'")
                # Cria um novo objeto funcionario
                novo_funcionario = Funcionario(df_funcionario.cpf.values[0], df_funcionario.nome.values[0])
                # Exibe os atributos do novo funcionario
                print(novo_funcionario.to_string())
                # Retorna o objeto novo_funcionario para utilização posterior, caso necessário
                #return novo_funcionario
                opcao = int(input("Deseja inserir mais funcionarios? 1-Sim 2-Não"))
            else:
                print(f"O CPF {cpf} já está cadastrado.")
                opcao = 3
                return None
        if opcao == 2:
            print("Retornando a tela principal")

    def atualizar_funcionario(self) -> Funcionario:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        opcao = 1
        while opcao == 1:

            # Solicita ao usuário o código do funcionario a ser alterado
            cpf = int(input("CPF do funcionario que deseja alterar o nome: "))

            # Verifica se o funcionario existe na base de dados
            if not self.verifica_existencia_funcionario(oracle, cpf):
                # Solicita a nova descrição do funcionario
                novo_nome = input("Nome (Novo): ")
                # Atualiza o nome do funcionario existente
                oracle.write(f"update funcionario set nome = '{novo_nome}' where cpf = {cpf}")
                # Recupera os dados do novo funcionario criado transformando em um DataFrame
                df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome from funcionario where cpf = {cpf}")
                # Cria um novo objeto funcionario
                funcionario_atualizado = Funcionario(df_funcionario.cpf.values[0], df_funcionario.nome.values[0])
                # Exibe os atributos do novo funcionario
                print(funcionario_atualizado.to_string())
                # Retorna o objeto funcionario_atualizado para utilização posterior, caso necessário
                #return funcionario_atualizado
                opcao = int(input("Deseja atualizar mais funcionarios? 1-Sim 2-Não"))
            else:
                print(f"O CPF {cpf} não existe.")
                opcao = 3
                return None
        if opcao == 2:
            print("Retornando a tela principal")

    def excluir_funcionario(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        opcao = 1

        while opcao == 1:
            # Solicita ao usuário o CPF do funcionario a ser alterado
            cpf = int(input("CPF do funcionario que irá excluir: "))        
            confirma = int(input("Tem certeza que deseja excluir?1-sim 2-não"))
            if confirma == 1:
                # Verifica se o funcionario existe na base de dados
                if not self.verifica_existencia_funcionario(oracle, cpf):            
                    # Recupera os dados do novo funcionario criado transformando em um DataFrame
                    df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome from funcionario where cpf = {cpf}")
                    # Revome o funcionario da tabela
                    oracle.write(f"delete from funcionario where cpf = {cpf}")            
                    # Cria um novo objeto funcionario para informar que foi removido
                    funcionario_excluido = Funcionario(df_funcionario.cpf.values[0], df_funcionario.nome.values[0])
                    # Exibe os atributos do funcionario excluído
                    print("Funcionario Removido com Sucesso!")
                    print(funcionario_excluido.to_string())
                    opcao = int(input("Deseja excluir mais funcionarios? 1-Sim 2-Não"))
                else:
                    print(f"O CPF {cpf} não existe.")
                    opcao = 3
            else:
                opcao = int(input("Deseja excluir mais funcionarios? 1-Sim 2-Não"))
        if opcao == 2:
            print("Retornando a tela principal")

    def verifica_existencia_funcionario(self, oracle:OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do novo funcionario criado transformando em um DataFrame
        df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome from funcionario where cpf = {cpf}")
        return df_funcionario.empty
