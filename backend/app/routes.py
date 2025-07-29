from flask import Blueprint, request, jsonify
from app.nlp.sentiment import analyze_sentiment
from app.nlp.topics import extract_topics
from app.nlp.preprocessing import clean_text
from app.nlp.improvement import suggest_improvement

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/analyze-feedback', methods=['POST'])
def analyze_feedback():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    cleaned = clean_text(text)
    sentiment = analyze_sentiment(cleaned)
    topics = extract_topics(cleaned)
    suggestions = suggest_improvement(topics)

    return jsonify({
        'cleaned_text': cleaned,
        'sentiment': sentiment,
        'topics': topics,
        'improvements': suggestions
    })
