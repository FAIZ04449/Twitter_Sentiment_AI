import re
import emoji
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure vader lexicon is available
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


# Slang dictionary
slang_dict = {
    "lit": "amazing",
    "bruh": "disappointed",
    "mid": "average",
    "fire": "excellent",
    "wtf": "angry",
    "omg": "surprised",
    "lol": "laughing",
    "lmao": "laughing",
    "idk": "confused"
}

def normalize_repeated_letters(text):
    # sooooo → soo
    return re.sub(r"(.)\1{2,}", r"\1\1", text)

def replace_slang(text):
    words = text.split()
    new_words = [slang_dict.get(word.lower(), word) for word in words]
    return " ".join(new_words)

def preprocess_text(text):
    # Convert emojis to words
    text = emoji.demojize(text)

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtag symbol but keep text
    text = re.sub(r"#", "", text)

    # Normalize repeated letters
    text = normalize_repeated_letters(text)

    # Replace slang
    text = replace_slang(text)

    # Remove extra spaces
    text = text.strip()

    return text

def analyze_sentiment(text):
    cleaned = preprocess_text(text)

    scores = sia.polarity_scores(cleaned)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "original_text": text,
        "cleaned_text": cleaned,
        "sentiment": sentiment,
        "compound_score": compound,
        "detailed_scores": scores
    }
