from flask import Flask, jsonify
app = Flask(__name__)
cafe_menu=[
    {"item": "Espresso", "price": 2.5},
    {"item": "Cappuccino", "price": 3.0},
    {"item": "Latte", "price": 3.5}
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(cafe_menu)
@app.route('/hello', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, World!'})
@app.route('/hello/<name>', methods=['GET'])
def personal_greet(name):
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)