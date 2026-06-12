from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def products():
    return jsonify([
        {"id": 1, "name": "Gaming Laptop", "price": 1499},
        {"id": 2, "name": "Mechanical Keyboard", "price": 129},
        {"id": 3, "name": "4K Monitor", "price": 399}
    ])

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
