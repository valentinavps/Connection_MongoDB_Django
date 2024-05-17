from pymongo import MongoClient  # importação do pymongo, biblioteca que possibilita a integração do python com o banco de dados
from .mongo_db_configs import mongo_db_infos  # certifique-se de que o caminho está correto
# from mongo_db_configs import mongo_db_infos
from urllib.parse import quote_plus  # uso do quote_plus para "traduzir" os símbolos gráficos na hora da leitura feita pelo MongoClient

class DBconnectionHandler:
    def _init_(self) -> None:  # construtora da classe DBconnectionHandler, responsável por gerenciar o controle da conexão
        username = mongo_db_infos["USERNAME"]  # pegar username do arquivo de configuração
        password = mongo_db_infos["PASSWORD"]  # pegar password do arquivo de configuração
        self.__connection_string = f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@cluster0.lb2khsh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.dbname = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):  # função para realizar a conexão inicial com banco de dados
        self._client = MongoClient(self._connection_string)
        self._db_connection = self._client[quote_plus(self.dbname)]  # onde a conexão ocorre, no banco escolhido dado por self.dbname

    def get_db_connection(self):  # retorno da conexão feita, útil para confirmar a conexão
        return self.__db_connection

    def get_db_client(self):
        return self.__client
