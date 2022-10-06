from conexion.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.qry_total_holerite = "select count(1) as total_holerite from holerite"
        self.qry_total_funcionario = "select count(1) as total_funcionario from funcionario"
        self.qry_total_empresa = "select count(1) as total_empresa from empresa"
        self.created_by = "Arthur Grinewald Ciro Massariol Gabrieli Mombrini Livia Hand Julio Godinho"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_holerite(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_holerite)["total_holerite"].values[0]

    def get_total_funcionario(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_funcionario)["total_funcionario"].values[0]
    
    def get_total_empresa(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_empresa)["total_empresa"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE RH                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - HOLERITES:         {str(self.get_total_holerite()).rjust(5)} 
        #      2 - FUNCIONARIOS:      {str(self.get_total_funcionario()).rjust(5)}
        #      3 - EMPRESAS:          {str(self.get_total_empresa()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
