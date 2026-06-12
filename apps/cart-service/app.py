from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def cart():
    return jsonify({
        "cart": [
            {"product": "Gaming Laptop", "quantity": 1},
            {"product": "Mechanical Keyboard", "quantity": 2}
        ],
        "message": "Cart service is running"
    })

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
