from Demos.win32ts_logoff_disconnected import username
from flask import Flask,render_template,request
'''
It create an interface of the Flask class,
which will be your WSGI (web server gateway interface) application.
'''

#--------WSGI Application--------------
app=Flask(__name__)

@app.route('/')
def welcome():
    return '<html><H1>welcome kaif</H1></html>'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html',methods=['GET'])
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}!"
    return render_template('form.html')
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}!"
    return render_template('form.html')
if __name__=='__main__':
    app.run(debug=True)