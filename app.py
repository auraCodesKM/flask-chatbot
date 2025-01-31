from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/run-ollama', methods=['POST'])
def run_ollama():
    data = request.get_json()  
    user_query = data.get('query')  
    if not user_query:
        return jsonify({'response': 'No query provided'}), 400
    
    cmd = f'echo "{user_query}" | ollama run llama2'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    return jsonify({'response': result.stdout.strip()})

if __name__ == "__main__":
    app.run(debug=True)
