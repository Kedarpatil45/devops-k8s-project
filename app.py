from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "DevOps K8s Project Running 🚀"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    # trigger workflow