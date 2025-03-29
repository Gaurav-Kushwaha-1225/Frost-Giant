from flask import Flask, request, jsonify
from models.llama3 import Llama3Model
from models.mistral import MistralModel

app = Flask(__name__)

llama_model = Llama3Model()
mistral_model = MistralModel()

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    model_name = data.get("model", "llama3")
    prompt = data.get("prompt", "")

    if model_name == "llama3":
        response = llama_model.generate_response(prompt)
    elif model_name == "mistral":
        response = mistral_model.generate_response(prompt)
    else:
        response = "Invalid model selection"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
