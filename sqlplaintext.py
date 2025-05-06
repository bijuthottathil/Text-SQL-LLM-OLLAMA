from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = 'http://localhost:11434/api/generate'
OLLAMA_MODEL = 'llama2'  # You can swap to mixtral, codellama, etc.

@app.route('/explain', methods=['POST'])
def explain_code():
    data = request.json
    code_block = data.get('code')
    code_type = data.get('type', 'SQL').upper()  # Default to SQL

    if not code_block:
        return jsonify({"error": "Missing 'code' in request"}), 400

    # Prepare prompt based on type
    if code_type == 'SQL':
        prompt = f"Explain the following SQL query in simple English:\n\n{code_block}"
    elif code_type == 'ETL':
        prompt = f"Explain the following ETL script (e.g., PySpark) in simple English:\n\n{code_block}"
    else:
        prompt = f"Explain the following code in simple English:\n\n{code_block}"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        ollama_response = response.json()
        explanation = ollama_response.get("response", "").strip()

        return jsonify({
            "input_type": code_type,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
