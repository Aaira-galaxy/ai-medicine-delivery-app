from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="YOUR_API_KEY")

@app.route("/")
def home():
    return "AI Medicine App Running 🚀"

@app.route("/explain-medicine", methods=["POST"])
def explain_medicine():
    data = request.json
    medicine = data.get("medicine")

    prompt = f"Explain how to use {medicine}, dosage, and side effects in simple language."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "explanation": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(debug=True)
