import mysql.connector

mydb = mysql.connector.connect(
  host="aws.connect.psdb.cloud",
  user="k6pcltr9zak07qx61jlo",
  password="pscale_pw_moBUflaanwmeGT6Wky984HALNzX2x9XMwTyBGCFCVVY")

cursor = mydb.cursor()


def load_data(t):
  query = "insert into project_database.operation_detail (num1 ,num2  ,operation , result ) values (%s,%s,%s,%s)"
  cursor.execute(query, t)
  mydb.commit()
