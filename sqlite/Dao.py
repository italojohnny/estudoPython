import sqlite3
import re

class Dao:
    def __init__ (self, db):
        self.conn = sqlite3.connect(db)
        self.conn.create_function("REGEXP", 2, self.regexp)

    def __del__ (self):
        self.conn.close()

    def regexp (regex, text):
        """ Ativa operador REGEXP nas intrucoes do sqlite. Retorna true quando casar; pode ser combinado com NOT
        EX: SELECT 'SQLite' REGEXP '^SQL';
            SELECT 'SQLite' NOT REGEXP '^SQL';
        """ 
        return re.search(re.compile(regex), text) is not None

    def query_list_dict (self, query):# {{{
        """ Retorna uma consulta em lista de dicionarios,
        onde as chaves sao os nomes das colunas da tabela.
        """
        def dict_factory (cursor, row):
            dictionary = {}
            for index, column in enumerate(cursor.description):
                dictionary[column[0]] = row[index]
            return dictionary

        result = []
        try:
            self.conn.row_factory = dict_factory
            result = self.conn.cursor().execute(query).fetchall()

        except Exception as error:
            print error

        finally:
            return result
# }}}

if __name__ == "__main__":
    dao = Dao("arquivo.db")
    for i in dao.query_list_dict("SELECT * FROM latlng;"):
        print i["dtRegister"]

    print "================"

    cursor = dao.conn.cursor()
    cursor.execute("SELECT * FROM latlng WHERE dtRegister REGEX '^2017-02-01 18:18:18';")
    data=cursor.fetchall()
    print(data)
