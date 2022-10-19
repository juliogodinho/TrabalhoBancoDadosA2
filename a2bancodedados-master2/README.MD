# Exemplo de Sistema em Python fazendo CRUD no Oracle

Para executar, bastar inserir o comando a seguir, o resto é intuitivo:
```shell
~$ python principal.py
```

## Organização
- [diagrams](diagrams): Nesse diretório está o [diagrama relacional](diagrams/RH.pdf) (lógico) do sistema.
    * O sistema possui três entidades: HOLERITE, FUNCIONARIOS, EMPRESAS
- [sql](sql): Nesse diretório estão os scripts para criação das tabelas e inserção de alguns dados fictícios para testes do sistema
    * [create_tables_rh.sql](sql/create_tables_rh.sql): script responsável pela criação das tabelas e relacionamentos
- [src](src): Nesse diretório estão os scripts do sistema
    * [conexion](src/conexion): Nesse repositório encontra-se o [módulo de conexão com o banco de dados Oracle](src/conexion/oracle_queries.py)
    * [controller](src/controller/): Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.
    * [model](src/model/): Nesse diretório encontram-se as classes das entidades descritas no [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_RH.pdf)
    * [reports](src/reports/) Nesse diretório encontra-se a [classe](src/reports/relatorios.py) responsável por gerar todos os relatórios do sistema
    * [sql](src/sql/): Nesse diretório encontram-se os scripts utilizados para geração dos relatórios a partir da [classe relatorios](src/reports/relatorios.py)
    * [utils](src/utils/): Nesse diretório encontram-se scripts de [configuração](src/utils/config.py) e automatização da [tela de informações iniciais](src/utils/splash_screen.py)

### Bibliotecas Utilizadas
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`

### Instalando Oracle InstantClient
- Baixe a versão do InstantClient de acordo com a versão do Banco de Dados
- Execute o comando a seguir, caso precise converter o arquivo .rpm para .deb
  ```shell
  sudo alien --scripts oracle-instantclient18.5-basic-18.5.0.0.0-3.x86_64.rpm
  ```
- Descompacte o arquivo e será gerado um diretório
- Mova o diretório para a localizaçõ correta:
  ```shell
  sudo mv instantclient_18_5 /usr/local/oracle/
  ```
- Mova os diretórios lib e share para dentro do diretório do InstantClient
  ```shell
  sudo mv lib instantclient_18_5/
  ```
  
  ```shell
  sudo mv share instantclient_18_5/
  ```
- Crie as seguintes variáveis de ambiente via terminal
  ```shell
  export ORACLE_HOME=/usr/local/oracle/instantclient_18_5
  ```

  ```shell
  export ORACLE_HOME=/usr/local/oracle/instantclient_18_5/lib/oracle/18.5/client64/lib
  ```
## Vídeo Descritivo
(vídeo demonstrativo)[]

## Contato
- [E-Mail](mailto:juliogodinho@gmail.com)

## Integrantes
Livia Hand Fraga;
Ciro Massariol de Araujo;
Júlio Godinho Carreira;
Arthur Grinevald Samico;
Gabrielli Mombrini Feletti.
