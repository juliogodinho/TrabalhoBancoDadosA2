from model.empresa import Empresa
from conexion.oracle_queries import OracleQueries

class Controller_empresa:
    def __init__(self):
        pass
        
    def inserir_empresa(self) -> Empresa:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
       
        opcao = 1
        while opcao == 1:
            # Solicita ao usuario o novo CNPJ
            cnpj = input("CNPJ (Novo): ")

            if self.verifica_existencia_empresa(oracle, cnpj):
                # Solicita ao usuario o novo nome
                nome_fantasia = input("Nome Fantasia (Novo): ")
                razao_social = input("Razao Social (Novo): ")
                # Insere e persiste a nova empresa
                oracle.write(f"insert into empresa values ('{cnpj}', '{nome_fantasia}', '{razao_social}')")
                # Recupera os dados da nova empresa criado transformando em um DataFrame
                df_empresa = oracle.sqlToDataFrame(f"select cnpj, nome_fantasia from empresa where cnpj = '{cnpj}'")
                # Cria um novo objeto empresa
                #novo_empresa = Empresa(df_empresa.cnpj.values[0], df_empresa.nome_fantasia.values[0])
                # Exibe os atributos do novo cliente
                #print(novo_empresa.to_string())
                # Retorna o objeto novo_empresa para utilização posterior, caso necessário
                #return novo_empresa
                print("CNPJ: ", cnpj)
                print("Nome Fantasia: ", nome_fantasia)
                print("Razao Social: ", razao_social)
                opcao = int(input("Deseja inserir mais empresas? 1-Sim 2-Não"))
            else:
                print(f"O CNPJ {cnpj} já está cadastrado.")
                opcao = 3
                return None
        if opcao == 2:
            print("Retornando a tela principal")

    def atualizar_empresa(self) -> Empresa:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        opcao = 1
        while opcao == 1:
            # Solicita ao usuário o código da empresa a ser alterada
            cnpj = int(input("CNPJ da empresa que deseja alterar o nome: "))

            # Verifica se a empresa existe na base de dados
            if not self.verifica_existencia_empresa(oracle, cnpj):
                # Solicita a nova descrição da empresa
                novo_nome = input("Nome Fantasia (Novo): ")
                novo_razaosocial = input("Razao Social (Novo): ")
                # Atualiza o nome da empresa existente
                oracle.write(f"update empresa set nome_fantasia = '{novo_nome}' where cnpj = {cnpj}")
                oracle.write(f"update empresa set razao_social = '{novo_razaosocial}' where cnpj = {cnpj}")
                # Recupera os dados do nova empresa criada transformando em um DataFrame
                df_empresa = oracle.sqlToDataFrame(f"select cnpj, nome_fantasia from empresa where cnpj = {cnpj}")
                # Cria um novo objeto empresa
                empresa_atualizado = Empresa(df_empresa.cnpj.values[0], df_empresa.nome_fantasia.values[0])
                # Exibe os atributos da nova empresa
                print(empresa_atualizado.to_string())
                # Retorna o objeto empresa_atualizado para utilização posterior, caso necessário
                #return empresa_atualizado
                opcao = int(input("Deseja atualizar mais empresas? 1-Sim 2-Não"))
            else:
                print(f"O CNPJ {cnpj} não existe.")
                opcao = 3
                return None
        if opcao == 2:
            print("Retornando a tela principal")

    def excluir_empresa(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        opcao = 1
        while opcao == 1:
            # Solicita ao usuário o CNPJ da empresa a ser alterado
            cnpj = int(input("CNPJ da empresa que irá excluir: "))        

            # Verifica se a empresa existe na base de dados
            if not self.verifica_existencia_empresa(oracle, cnpj):            
                # Recupera os dados da nova empresa criada transformando em um DataFrame
                df_empresa = oracle.sqlToDataFrame(f"select cnpj, nome_fantasia from empresa where cnpj = {cnpj}")
                # Revome a empresa da tabela
                oracle.write(f"delete from empresa where cnpj = {cnpj}")            
                # Cria um novo objeto empresa para informar que foi removido
                empresa_excluido = Empresa(df_empresa.cnpj.values[0], df_empresa.nome_fantasia.values[0])
                # Exibe os atributos da empresa excluída
                print("Empresa Removida com Sucesso!")
                print(empresa_excluido.to_string())
                opcao = int(input("Deseja excluir mais empresas? 1-Sim 2-Não"))
            else:
                print(f"O CNPJ {cnpj} não existe.")
                opcao = 3
        if opcao == 2:
            print("Retornando a tela principal")

    def verifica_existencia_empresa(self, oracle:OracleQueries, cnpj:str=None) -> bool:
        # Recupera os dados da nova empresa criado transformando em um DataFrame
        df_empresa = oracle.sqlToDataFrame(f"select cnpj, nome_fantasia from empresa where cnpj = {cnpj}")
        return df_empresa.empty
