# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    year = (datetime.now().year) - 1998 #nice
    return render_template('index.html', year = year)


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(port=4000, debug=True)
