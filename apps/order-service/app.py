from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def orders():
    return jsonify({
        "orders": [
            {
                "order_id": 1001,
                "status": "Processing",
                "total": 1499
            },
            {
                "order_id": 1002,
                "status": "Shipped",
                "total": 528
            }
        ]
    })

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
