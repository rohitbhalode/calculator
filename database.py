import mysql.connector

mydb = mysql.connector.connect(
  host="aws.connect.psdb.cloud",
  user="hkl7br5agb1i5p6bx39s",
  password="pscale_pw_FDlkret3Ozjgoh9QJYKratgTxKoCas5NcVCPnDT7goW")

cursor = mydb.cursor()
query = "insert into project_database.pidea (yname,idea) values (%s,%s)"

cursor.execute(query, ('Rohit', "fsf"))
mydb.commit()


def load_data(t):
  query = "insert into project_database.operation_detail (num1 ,num2  ,operation , result ) values (%s,%s,%s,%s)"
  cursor.execute(query, t)
  mydb.commit()
