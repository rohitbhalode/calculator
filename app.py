from flask import Flask, render_template, request
from database import load_data
app = Flask(__name__)


@app.route("/")
def welcome():
  return render_template("index.html")


@app.route("/submit", methods=['POST'])
def result():
  num1 = float(request.form.get("num1"))
  num2 = float(request.form.get("num2"))
  op = request.form.get("operation")
  result=None
  if (op == "sum"):
    result=num1+num2
  elif (op == "sub"):
    result=num1 - num2
  elif (op == "mul"):
    result=num1 * num2
  else:
    result=num1 / num2
  t=(num1,num2,op,result)
  load_data(t)
  return render_template("result.html")


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
