from flask import Flask, request, render_template
import random


app=Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['POST',
'GET'])
def base_page():
 
  if request.method =='POST':
    dogs = request.form['dogs']
    return render_template('index.html', dogs=dogs)
  
  if request.method =='GET':
    dogs="1"
    return render_template('index.html', dogs=dogs)
if __name__=="__main__":
  app.run(host='127.0.0.1', port=random.randint(2000, 9000))
