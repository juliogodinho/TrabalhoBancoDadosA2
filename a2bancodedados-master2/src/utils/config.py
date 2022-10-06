MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatório de Holerite
2 - Relatório de Funcionarios
3 - Relatório de Empresas
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - HOLERITE
2 - FUNCIONARIOS
3 - EMPRESAS
"""

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")
