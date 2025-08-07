from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="templates")

# ✅ Replace with your actual Google Gemini API Key
GEMINI_API_KEY = "AIzaSyBnDf1W6kbFd7wldJY2oeSmM0dv3HNkICc"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask_gemini', methods=['POST'])
def ask_gemini():
    user_input = request.json.get("query")

    if not user_input:
        return jsonify({"response": "Error: No input provided."}), 400

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [{"parts": [{"text": user_input}]}]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response_data = response.json()

        # ✅ Extract the correct response format from Gemini
        if "candidates" in response_data and response_data["candidates"]:
            gemini_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"response": gemini_response})
        else:
            return jsonify({"response": "Error: Invalid response format from Gemini."})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"response": f"Request Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
