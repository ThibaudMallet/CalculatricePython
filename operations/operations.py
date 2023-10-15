from flask import jsonify

def add(num1, num2):
    result = round(num1 + num2, 2)
    return jsonify({"result": result}), 200

def substract(num1, num2):
    result = round(num1 - num2, 2)
    return jsonify({"result": result}), 200

def multiply(num1, num2):
    result = round(num1 * num2, 2)
    return jsonify({"result": result}), 200

def divide(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if num2 == 0:
            return jsonify({"error": "La division par 0 est impossible"}), 400
        
        result = round(num1 / num2, 2)
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "Données incorrectes"}), 400