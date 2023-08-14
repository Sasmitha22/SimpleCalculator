from flask import Flask, request, jsonify ,render_template
app = Flask(__name__)
from cal import calculator
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    op = str(request.form['operation'])
    result = calculator(a,b,op)
    return render_template('index.html', prediction_text = str(result))

if __name__ == '__main__':
    app.run()