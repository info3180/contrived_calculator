import os
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)


@app.route("/")                         # you can attach multiple routes to
@app.route("/<myname>")                 # one function
def hello(myname='person'):
  #return "Hello {0}".format(myname)
  return render_template('index.html',myname=myname)
  
# converters modify the dynamic part before it is passed to the function.
# int,float & path are built-in converters. Custom converters can be added.


@app.route('/2257.png')
def send_2257():
    """Send your static text file."""
    
    return app.send_static_file('2257.png')  # checks the static folder by default

@app.route("/int-add/<int:a>/<int:b>",methods=['GET', 'POST'])   #try this with floats. Whys wont it work?
def int_add(a,b):
  result = str(a + b)
  if request.method == 'POST':
     return jsonify(dict(result=result))
  return render_template('answer.html',answer=result)


@app.route("/float-add/<float:a>/<float:b>",methods=['GET', 'POST']) 
def float_add(a,b):
  result = str(a + b)
  if request.method == 'POST':
     return jsonify(dict(result=result))
  return render_template('answer.html',answer=result)

@app.route("/calc/<a>/<opperand>/<b>" ,methods=['GET', 'POST'])
def calc(opperand,a,b):
  a,b= float(a),float(b)
  
  if opperand in ('+','plus','and'):
    result = str(a + b)
  if opperand in  ('-','minus'):
    result = str(a - b)
  if opperand in  ('*','multiply','times'):
    result = str(a * b)
  if request.method == 'POST':
     return jsonify(dict(result=result))
  return render_template('answer.html',answer=result)
  
if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("IP", '0.0.0.0'),port=int(os.getenv("PORT", 8080) ))
