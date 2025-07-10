from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

@app.route('/task01', methods=['POST'])
def count_words():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400
    word_count = len(data['text'].split())
    return jsonify({'word_count': word_count})

@app.route('/task02', methods=['POST'])
def count_characters():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400
    text = data['text'].replace(" ", "")
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return jsonify({'frequencies': dict(freq)})

if __name__ == '__main__':
    app.run(debug=True)