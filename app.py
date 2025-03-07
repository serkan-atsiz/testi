from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertModel

app = Flask(__name__)

# Hugging Face Transformers modelini yükleyin
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    inputs = tokenizer.encode_plus(text, return_tensors='pt')
    outputs = model(**inputs)
    result = outputs.last_hidden_state[:, 0, :]
    return jsonify({'result': result.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
