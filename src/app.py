from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST','GET'])
def enviar():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']

        return jsonify({'name': name, 'email': email, 'number': number})
    return 'metodo no permitodo', 405


if __name__ == '__main__':
    app.run(debug=True)