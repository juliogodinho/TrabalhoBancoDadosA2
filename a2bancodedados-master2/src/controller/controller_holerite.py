import cProfile
from pydoc import cli
from model.holerite import Holerite
from model.funcionario import Funcionario
from controller.controller_funcionario import Controller_funcionario
from model.empresa import Empresa
from controller.controller_empresa import Controller_empresa
from conexion.oracle_queries import OracleQueries
from datetime import date

class Controller_holerite:
    def __init__(self):
        self.ctrl_funcionario = Controller_funcionario()
        self.ctrl_empresa = Controller_empresa()
        
    def inserir_holerite(self) -> Holerite:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        # Cria uma nova conexão com o banco
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        #oracle = OracleQueries()
        codigo = int
        
        opcao = 1
        while opcao == 1:
            # Lista os funcionarios existentes para inserir na holerite
            self.listar_funcionario(oracle, need_connect=True)
            cpf = str(input("Digite o número do CPF do Funcionario: "))
            funcionario = self.valida_funcionario(oracle, cpf)
            if funcionario == None:
                return None

            # Lista as empresas existentes para inserir na holerite
            self.listar_empresa(oracle, need_connect=True)
            cnpj = str(input("Digite o número do CNPJ da Empresa: "))
            empresa = self.valida_empresa(oracle, cnpj)
            if empresa == None:
                return None


            #codigo = input("Codigo (Novo): ")
            #cursor = oracle.connect()
            #output_value = cursor.var(int)
            #data = dict(codigo=output_value)
            #cursor.execute("""
            #begin
            #    :codigo := HOLERITE_CODIGO_SEQ.NEXTVAL;
            #    insert into holerite values(:codigo);
            #end;
            #""", data)
            #codigo = output_value.getvalue()
            #cpf=funcionario.get_CPF()
            #cnpj=empresa.get_CNPJ()
            #codigo = output_value.getvalue()
            #:codigo := HOLERITE_CODIGO_HOLERITE_SEQ.NEXTVAL;
            # Cria um dicionário para mapear as variáveis de entrada e saída
            #data = dict(codigo=output_value, cpf=funcionario.get_CPF(), cnpj=empresa.get_CNPJ())
            # Executa o bloco PL/SQL anônimo para inserção do novo produto e recuperação da chave primária criada pela sequence
            # Recupera o código da nova holerite
            #codigo = output_value.getvalue()
            # Persiste (confirma) as alterações
            #oracle.conn.commit()
            # Solicita ao usuario o novo nome
            salariobruto = float(input("Salariobruto (Novo): "))
            fgts = float(input("fgts (Novo): "))
            irpf = float(input("irpf (Novo): "))
            salarioliquido = float(input("salarioliquido (Novo): "))
            # Insere e persiste a nova empresa
            oracle.write(f"insert into holerite values ((select nvl(max(codigo),0) + 1 from holerite), '{cpf}', '{cnpj}', '{salariobruto}', '{fgts}', '{irpf}', '{salarioliquido}')")
            # Recupera os dados da nova empresa criado transformando em um DataFrame
            #df_holerite = oracle.sqlToDataFrame(f"select codigo, salariobruto from holerite where codigo = '{codigo}'")
            # Cria um novo objeto holerite
            #novo_holerite = Holerite(df_holerite.codigo.values[0], funcionario, empresa)
            # Exibe os atributos da nova holerite
            #print(novo_holerite.to_string())
            # Retorna o objeto novo_empresa para utilização posterior, caso necessário
            print("CPF: ", cpf)
            print("CNPJ: ", cnpj)
            #print("Codigo: ", codigo)
            opcao = int(input("Deseja inserir mais holerites? 1-Sim 2-Não"))
        if opcao == 2:
            print("Retornando a tela principal")

    def atualizar_holerite(self) -> Holerite:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        opcao = 1
        while opcao == 1:
            # Solicita ao usuário o código da holerite a ser alterada
            codigo = int(input("Código da Holerite que irá alterar: "))        

            # Verifica se o produto existe na base de dados
            if not self.verifica_existencia_holerite(oracle, codigo):

                # Lista os funcionarios existentes para inserir na holerite
                self.listar_funcionario(oracle)
                cpf = str(input("Digite o número do CPF do Funcionario: "))
                funcionario = self.valida_funcionario(oracle, cpf)
                if funcionario == None:
                    return None

                # Lista as empresas existentes para inserir na holerite
                self.listar_empresa(oracle)
                cnpj = str(input("Digite o número do CNPJ da empresa: "))
                empresa = self.valida_empresa(oracle, cnpj)
                if empresa == None:
                    return None

                data_hoje = date.today()

                            # Solicita ao usuario o novo nome
                salariobruto = float(input("Salariobruto (Novo): "))
                fgts = float(input("fgts (Novo): "))
                irpf = float(input("irpf (Novo): "))
                salarioliquido = float(input("salarioliquido (Novo): "))
                # Atualiza a descrição da holerite existente
                oracle.write(f"update holerite set salariobruto = '{salariobruto}', fgts = '{fgts}', irpf = '{irpf}', salarioliquido = '{salarioliquido}' where codigo = {codigo}")
                # Recupera os dados da nova holerite criada transformando em um DataFrame
                #df_holerite = oracle.sqlToDataFrame(f"select codigo, from holerite where codigo = {codigo}")
                # Cria um novo objeto Holerite
                #holerite_atualizado = Holerite(df_holerite.codigo.values[0], df_holerite.salariobruto.values[0])
                # Exibe os atributos do novo produto
                #print(holerite_atualizado.to_string())
                # Retorna o objeto holerite_atualizado para utilização posterior, caso necessário
                #return holerite_atualizado
                print("CPF: ", cpf)
                print("CNPJ: ", cnpj)
                print("Codigo: ", codigo)
                opcao = int(input("Deseja atualizar mais holerites? 1-Sim 2-Não"))
            else:
                print(f"O código {codigo} não existe.")
                opcao = int(input("Deseja atualizar mais holerites? 1-Sim 2-Não"))
                #return None
        if opcao == 2:
            print("Retornando a tela principal")

    def excluir_holerite(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        opcao = 1
        while opcao == 1:
            # Solicita ao usuário o código da holerite a ser excluida
            codigo = int(input("Código da Holerite que irá excluir: "))        

            # Verifica se o produto existe na base de dados
            if not self.verifica_existencia_holerite(oracle, codigo):            
                # Recupera os dados do nova holerite criado transformando em um DataFrame
                #df_holerite = oracle.sqlToDataFrame(f"select codigo, salariobruto, fgts, irpf, salarioliquido from holerite where codigo = {codigo}")
                #funcionario = self.valida_funcionario(oracle, df_holerite.cpf.values[0])
                #empresa = self.valida_empresa(oracle, df_holerite.cnpj.values[0])
 
                # Revome a holerite
                oracle.write(f"delete from holerite where codigo = {codigo}")
                # Cria um novo objeto Produto para informar que foi removido
                #holerite_excluido = Holerite(df_holerite.codigo.values[0], df_holerite.salariobruto.values[0])
                # Exibe os atributos do produto excluído
                print("Holerite Removida com Sucesso!")
                print("Codigo da Holerite excluida: ", codigo)
                #print(holerite_excluido.to_string())
                opcao = int(input("Deseja excluir mais holerites? 1-Sim 2-Não"))
                    
            else:
                print(f"O código {codigo} não existe.")
                opcao = int(input("Deseja excluir mais holerites? 1-Sim 2-Não"))
        if opcao == 2:
            print("Retornando a tela principal")

    def verifica_existencia_holerite(self, oracle:OracleQueries, codigo:int=None) -> bool:
        # Recupera os dados da nova holerite criada transformando em um DataFrame
        df_holerite = oracle.sqlToDataFrame(f"select codigo, salariobruto from holerite where codigo = {codigo}")
        return df_holerite.empty

    def listar_funcionario(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select f.cpf
                    , f.nome 
                from funcionario f
                order by f.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_empresa(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select e.cnpj
                    , e.razao_social
                    , e.nome_fantasia
                from empresa e
                order by e.nome_fantasia
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_funcionario(self, oracle:OracleQueries, cpf:str=None) -> Funcionario:
        if self.ctrl_funcionario.verifica_existencia_funcionario(oracle, cpf):
            print(f"O CPF {cpf} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_funcionario = oracle.sqlToDataFrame(f"select cpf, nome from funcionario where cpf = {cpf}")
            # Cria um novo objeto cliente
            funcionario = Funcionario(df_funcionario.cpf.values[0], df_funcionario.nome.values[0])
            return funcionario

    def valida_empresa(self, oracle:OracleQueries, cnpj:str=None) -> Empresa:
        if self.ctrl_empresa.verifica_existencia_empresa(oracle, cnpj):
            print(f"O CNPJ {cnpj} informado não existe na base.")
            return None
        else:
            oracle.connect()
            # Recupera os dados do novo fornecedor criado transformando em um DataFrame
            df_empresa = oracle.sqlToDataFrame(f"select cnpj, razao_social, nome_fantasia from empresa where cnpj = {cnpj}")
            # Cria um novo objeto fornecedor
            empresa = Empresa(df_empresa.cnpj.values[0], df_empresa.razao_social.values[0], df_empresa.nome_fantasia.values[0])
            return empresa