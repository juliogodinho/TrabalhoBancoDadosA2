from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_holerite.sql") as f:
            self.query_relatorio_holerite = f.read()
            
        with open("sql/relatorio_funcionario.sql") as f:
            self.query_relatorio_funcionario = f.read()
            
        with open("sql/relatorio_empresa.sql") as f:
            self.query_relatorio_empresa = f.read()

    def get_relatorio_holerite(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_holerite))
        input("Pressione Enter para Sair do Relatório de Holerites")
        
    def get_relatorio_funcionario(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_funcionario))
        input("Pressione Enter para Sair do Relatório de Funcionarios")
        
    def get_relatorio_empresa(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_empresa))
        input("Pressione Enter para Sair do Relatório de Empresas")
