import sqlite3

database = "./faculty.db"
query_create_db = 'create_db_sql.sql'


class DB_server:

  def __init__(self, database):
    self.database = database

    ## create connection
    with sqlite3.connect(database) as con:
      self.cur = con.cursor()

  def execute(self, sql):
    self.cur.executescript(sql)

  def execute_query(self, sql):
    self.cur.execute(sql)
    return self.cur.fetchall()


if __name__ == "__main__":

  server = DB_server(database)
  with open(query_create_db, 'r') as f:
    sql = f.read()

  server.execute(sql)
