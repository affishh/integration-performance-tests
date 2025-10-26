from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Example.com!", 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    # Simulate processing time
    time.sleep(0.5)
    
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulate a data fetch
    time.sleep(0.2)
    return jsonify({"data": [1, 2, 3, 4, 5]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
