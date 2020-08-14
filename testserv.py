from flask import Flask, render_template, request
from func_name import name

app = Flask(__name__)

# base = {'Jack':'Martins'}

@app.route('/')
def main_page():
    return 'Main page'


@app.route('/first')
def page_first():
    return render_template('first.html')

@app.route('/name_func', methods=['POST'])
def do_name():
    name_user = request.form['name_field']
    return name(name_user)


app.run(debug=True)