
from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import analyze_review

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    review = data.get("review")
    if not review:
        return jsonify({"error": "No review provided"}), 400
    result = analyze_review(review)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
