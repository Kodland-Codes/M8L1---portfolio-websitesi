# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime

year = (datetime.now().year) - 2010 #nice

app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python,
                           year = year)


if __name__ == "__main__":
    app.run(port=4000, debug=True)
