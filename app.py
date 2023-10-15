from flask import Flask, request, jsonify, render_template
from operations import operations

app = Flask(__name__)

@app.route('/')
def show_calculator():
    return render_template('calculator.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1        = float(request.form.get('num1'))
    num2        = float(request.form.get('num2'))
    operation   = request.form.get('operation')

    try:        
        if operation == 'add':
            return operations.add(num1, num2)
        elif operation == 'substract':
            return operations.substract(num1, num2)
        elif operation == 'multiply':
            return operations.multiply(num1, num2)
        elif operation == 'divide':
            return operations.divide(num1, num2)
        else:
            return jsonify({'error': 'Opération non valide'}), 400
    except (ValueError, ZeroDivisionError):
        return jsonify({"error": "Impossible de diviser par 0"}), 400

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page non trouvée"}), 404

if __name__ == '__main__':
    app.run()