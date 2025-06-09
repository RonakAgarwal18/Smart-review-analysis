
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from keybert import KeyBERT
from utils import assign_aspect

sia = SentimentIntensityAnalyzer()
kw_model = KeyBERT()

def get_sentiment(review):
    score = sia.polarity_scores(review)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_review(review_text):
    sentiment = get_sentiment(review_text)
    keywords = [kw[0] for kw in kw_model.extract_keywords(review_text, 
                                                          keyphrase_ngram_range=(1, 2),
                                                          stop_words='english',
                                                          top_n=2)]
    aspect = assign_aspect(keywords)
    return {
        "review": review_text,
        "sentiment": sentiment,
        "keywords": keywords,
        "aspect": aspect
    }
