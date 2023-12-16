# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime



app = Flask(__name__)
year = 500

# İçerik sayfasını çalıştırma
@app.route('/ev')
def index():
    return render_template('index.html')


@app.route('/about_me')
def about():
    return render_template('about.html')



# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)




if __name__ == "__main__":
    app.run(port=4000, debug=True)
