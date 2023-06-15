import create_db
import fill_data

SUBJECTS = [
  "Mathematics", "Literature", "Geography", "Music", "Geometry", "Programming",
  "Lingustics", "History", "Biology", "Chemistry"
]

if __name__ == "__main__":

  server = create_db.DB_server(create_db.database)
  with open(create_db.query_create_db, 'r') as f:
    sql = f.read()

  ## create tables
  ###################print(sql)
  server.execute(sql)

  ## fill group table
  for num in range(fill_data.NUMBER_GROUPS):
    group_name = "G-" + str(num + 1)
    ##print(group_name)
    sql = "INSERT INTO groups(group_name) VALUES (\"" + group_name + "\")"
    ###################print(sql + ";")
    server.execute(sql)

  ## fill proffs table
  gen = fill_data.DataGenerator(fill_data.NUMBER_PROFS, fill_data.NAME)
  names = gen.generate()
  for name in names:
    ###print(name)
    sql = "INSERT INTO proffessors(proffessor_name) VALUES (\"" + name + "\")"
    #############################print(sql + ";")
    server.execute(sql)

  ## fill students table
  gen = fill_data.DataGenerator(fill_data.NUMBER_STUDENTS, fill_data.NAME)
  names = gen.generate()
  for name in names:
    ###print(name)
    group_id = gen.group_generator()
    sql = "INSERT INTO students(student_name,student_group) VALUES (\"" + name + "\"," + str(
      group_id) + ")"
    #############################3print(sql + ";")
    server.execute(sql)

  ## fill subjects table
  for name in fill_data.SUBJECTS:
    proff_id = gen.proff_generator()
    sql = "INSERT INTO subjects(subject_name,proffessor_id) VALUES (\"" + name + "\"," + str(
      proff_id) + ")"
    ##############################print(sql + ";")
    server.execute(sql)

  ## fill marks table
  for num in range(fill_data.MAX_MARKS):
    for student_id in range(1, fill_data.NUMBER_STUDENTS):
      mark = gen.mark_generator()
      subject_id = gen.subject_generator()
      sql = "INSERT INTO marks(student_id,subject_id,mark) VALUES (" + str(
        student_id) + "," + str(subject_id) + "," + str(mark) + ")"
      #################################  print(sql + ";")
      server.execute(sql)

  ## execute query#1
  print("query#1")
  with open("query_1.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#2
  print("query#2")
  with open("query_2.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#3
  print("query#3")
  with open("query_3.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#4
  print("query#4")
  with open("query_4.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#5
  print("query#5")
  with open("query_5.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#6
  print("query#6")
  with open("query_6.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#7
  print("query#7")
  with open("query_7.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#8
  print("query#8")
  with open("query_8.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#9
  print("query#9")
  with open("query_9.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))

  ## execute query#10
  print("query#10")
  with open("query_10.sql", 'r') as f:
    sql = f.read()
    print(server.execute_query(sql))
