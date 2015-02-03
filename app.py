import os
from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")                         # you can attach multiple routes to
@app.route("/<myname>")                 # one function
def hello(myname='person'):
  #return "Hello {0}".format(myname)
  return render_template('index.html',myname=myname)
  
# converters modify the dynamic part before it is passed to the function.
# int,float & path are built-in converters. Custom converters can be added.

@app.route("/int-add/<int:a>/<int:b>")  #try this with floats. Whys wont it work?
def int_add(a,b):
  return str(a + b)

@app.route("/float-add/<float:a>/<float:b>") 
def float_add(a,b):
  return str(a + b)

@app.route("/calc/<a>/<opperand>/<b>")
def calc(opperand,a,b):
  a,b= float(a),float(b)
  
  if opperand in ('+','plus','and'):
    return str(a + b)
  if opperand in  ('-','minus'):
    return str(a - b)
  if opperand in  ('*','multiply','times'):
    return str(a * b)
  
if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("IP", '0.0.0.0'),port=int(os.getenv("PORT", 8080) ))