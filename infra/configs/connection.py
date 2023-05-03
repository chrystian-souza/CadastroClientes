from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self):
        #Dados de endereço do banco de dados
        self.__connection_string = 'mysql+pymysql://root:Senac2021@localhost:3306/clientes'
        #Instância da engine(gerenciador do banco)
        self.__engine = self.__create_data_base_engine()
        #Sessão nula para que possa ser alocada uma nova ao ser instanciado um obj
        self.session = None
        #Validação da existencia do banco de dados
        self.__create_database()

    #Método para validação da existencia do banco de dados, caso não exista
    def create_database(self):
        engine = create_engine(self.__connection_string, echo=True)
        try:
            engine.connect()
        except Exception as e:
            if '1049' in str(e):
                engine = create_engine(self.__connection_string.rsplit('/', 1)[0], echo=True)
                conn = engine.connect()
                conn.execute(f'CREATE DATABASE IF NOT EXISTS {self.__connection_string.rsplit("/", 1)[1]}')
                conn.close()
                print('Banco criado')
            else:
                raise e

#Função para criação da engine sem necessidade de informar dados de endereço do banco e utilização de queryes escritas a mão
    def __create_engine(self):
        engine = create_engine(self.__connection_string, echo=True)

    def get_engine(self):
        return self.__engine

    #Funções mágicas que definem qualquer comportamento ao serem geradas instâncias
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        print('Gerando conexão')
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando conexão')
        self.session.close()

