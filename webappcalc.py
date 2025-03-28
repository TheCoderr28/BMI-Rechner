from flask import Flask, render_template, request

app = Flask(__name__)

# Hauptseite
@app.route('/')
def index():
    return render_template('index.html')

# Berechnungsseite
@app.route('/calculate', methods=['POST'])
def calculate():
    gewicht = float(request.form['gewicht'])
    groesse = float(request.form['groesse'])
    bmi = gewicht / (groesse ** 2)
    return render_template('result.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)