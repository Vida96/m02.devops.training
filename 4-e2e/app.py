from flask import Flask, jsonify, request

app = Flask(__name__)

history_data = []  # This will store the history of operations

@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add", methods=["POST"])
def add():
    history_data.append({"operation": "add", "a": request.json["a"], "b": request.json["b"], "result": request.json["a"] + request.json["b"]})
    return jsonify({"result": request.json["a"] + request.json["b"]}) 

@app.route("/subtract", methods=["POST"])
def subtract():
    history_data.append({"operation": "subtract", "a": request.json["a"], "b": request.json["b"], "result": request.json["a"] - request.json["b"]})
    return jsonify({"result": request.json["a"] - request.json["b"]})


@app.route("/multiply", methods=["POST"])
def multiply():
    history_data.append({"operation": "multiply", "a": request.json["a"], "b": request.json["b"], "result": request.json["a"] * request.json["b"]})
    return jsonify({"result": request.json["a"] * request.json["b"]})


@app.route("/divide", methods=["POST"])
def divide():
    history_data.append({"operation": "divide", "a": request.json["a"], "b": request.json["b"], "result": None if request.json["b"] == 0 else request.json["a"] / request.json["b"]})
    if request.json["b"] == 0:
        return jsonify({"result": "Division by zero is not allowed"}), 400
    return jsonify({"result": request.json["a"] / request.json["b"]})

@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": history_data})

if __name__ == "__main__":
    app.run(debug=True)
