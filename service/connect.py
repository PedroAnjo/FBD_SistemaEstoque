import psycopg2

class connectDataBase:
    def __init__(self):
       self.connection = psycopg2.connect(
            host = 'localhost',
            database = 'FBD_sistema_estoque',
            user = 'postgres',
            password = 'admin',
        )
       
    def get_instance(self):
        return self.connection
    
    def init_table(self):
        return

        