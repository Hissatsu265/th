from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the sentiment analysis API!"}), 200

@application.route('/api/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    blob = TextBlob(text)
    sentiment = blob.sentiment

    response = {
        "polarity": sentiment.polarity,   
        "subjectivity": sentiment.subjectivity  
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)