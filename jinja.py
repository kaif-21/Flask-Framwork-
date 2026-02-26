# Building Url Dynamically
# variable rules
# jinja 2 Template Engine
# jinja2 Template Engine
'''
{{ }} expression to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
# from Demos.win32ts_logoff_disconnected import username
from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def welcome():
    return '<h1>Welcome Kaif</h1>'

# Index Page
@app.route('/index')
def index():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Form Page (GET + POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello {name}!"
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=[]
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('success.html', result=res)

# Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp={'score':score,"res":res}

    return render_template('success.html', result=exp)


# if condition
@app.route('/successive/<int:score>')
def successive(score):


    return render_template('success.html', result=score)



if __name__ == '__main__':
    app.run(debug=True)