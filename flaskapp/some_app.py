print("Hello world!")
from flask import Flask
app = Flask(__name__)

#декоратор для вывода страницы по умолчанию

@app.route("/")
def hello():
  return " <html><head></head> <body> Hello World! </body></html>"

if __name__ == "__main__":
  app.run(host='127.0.0.1',port=5000)

from flask import render_template
@app.route("/data_to")
def data_to():
  #make value with data for translating in template
  some_pars = {'user':'Ivan','color':'red'}
  some_str = 'Hello my dear friends!'
  some_value = 10
  #translate data in template and run it
  return render_template('simple.html',some_str=some_str,some_value=some_value,some_pars=some_pars)
