from flask import Flask, request, jsonify
import psycopg2
import requests

app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'database': 'postgres',
    'port': 5432,
    'user': 'bijum',
    'password': 'yourpassword'  # Replace with your actual password
}

OLLAMA_URL = 'http://localhost:11434/api/generate'
OLLAMA_MODEL = 'llama2'

# Predefine schema info (you can also query it dynamically if needed)
SCHEMA_INFO = """
Tables:

1️⃣ customers:
- id (serial, PK)
- name (varchar)
- email (varchar)
- city (varchar)
- signup_date (date)

2️⃣ products:
- id (serial, PK)
- name (varchar)
- price (decimal)
- category (varchar)
- stock_quantity (int)

3️⃣ weather:
- id (serial, PK)
- city (varchar)
- temperature_celsius (decimal)
- humidity_percent (decimal)
- weather_condition (varchar)
- recorded_at (timestamp)
"""

PROMPT_TEMPLATE = """
You are an expert SQL assistant. Convert the natural language query below into a syntactically correct PostgreSQL SQL query.

{schema}

Important:
- Only generate the SQL query (no explanations).
- Default to safe SELECT queries unless instructed otherwise.

Natural language query:
"{nl_query}"

SQL query:
"""

@app.route('/text-to-sql', methods=['POST'])
def text_to_sql():
    data = request.json
    nl_query = data.get('query')

    if not nl_query:
        return jsonify({"error": "Missing 'query' in request"}), 400

    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA_INFO,
        nl_query=nl_query
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        ollama_data = response.json()
        sql_query = ollama_data.get("response", "").strip()

        # Safety: Only allow SELECT by default
        if not sql_query.lower().startswith("select"):
            return jsonify({
                "warning": "Generated query is not a SELECT. Review before running!",
                "generated_sql": sql_query
            })

        # Execute SQL
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_query)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                results = [dict(zip(columns, row)) for row in rows]

        return jsonify({
            "natural_language": nl_query,
            "generated_sql": sql_query,
            "results": results
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
