from flask import Flask, render_template, session, redirect, request 
import random
app = Flask(__name__)
app.secret_key = 'secret_key'

total_gold= 0

@app.route('/')
def index(): 
    message = ""
    return render_template("index.html", message= message, total_gold=session['total_gold']) 

@app.route('/process_money', methods= ['POST']) 
def gainlose():
    try:
        session['total_gold']
    except KeyError:
        session['total_gold'] 
    if request.form['building'] == 'farm':
        print(session['total_gold'])
        session['total_gold'] = int(session['total_gold']) + random.randint(10,20)
        print(session['total_gold'])
        return redirect('/')
    if request.form['building'] == 'cave':
        print(session['total_gold'])
        session['total_gold'] = int(session['total_gold']) + random.randint(5,10)
        print(session['total_gold'])
        return redirect('/')
    if request.form['building'] == 'house':
        print(session['total_gold'])
        session['total_gold'] = int(session['total_gold']) + random.randint(2,5)
        print(session['total_gold'])
        return redirect('/')
    if request.form['building'] == 'casino':
        print(session['total_gold'])
        session['total_gold'] = int(session['total_gold']) + random.randint(-50,50)
        print(session['total_gold'])
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True)



