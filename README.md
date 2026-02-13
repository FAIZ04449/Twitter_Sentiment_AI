# 🐦 Twitter Sentiment AI
A Robust NLP-Based Sentiment Analysis System for Twitter Data

---

## 📌 Project Overview

Twitter Sentiment AI is an intelligent Natural Language Processing (NLP) system designed to classify tweets into:

- ✅ Positive  
- ❌ Negative  
- ➖ Neutral  

The system is specifically optimized for noisy social media text including emojis, slang, hashtags, grammatical inconsistencies, and informal language.

This project demonstrates applied NLP techniques using:

- NLTK (VADER Sentiment Analyzer)
- Custom Text Preprocessing Pipeline
- Emoji Normalization
- Slang Expansion
- FastAPI Backend
- Twitter-inspired UI

---

## 🚀 Key Features

✔ Real-time sentiment classification  
✔ Emoji-aware sentiment detection  
✔ Slang normalization (e.g., "lit", "bruh", "mid")  
✔ Removal of URLs, mentions, hashtags  
✔ Repeated character normalization (soooo → soo)  
✔ Clean Twitter-inspired user interface  
✔ REST API architecture  
✔ Robust preprocessing pipeline  

---

## 🧠 NLP Techniques Used

### 1️⃣ Text Preprocessing Pipeline

To improve sentiment accuracy on noisy Twitter data, the following preprocessing steps were implemented:

- URL removal
- Mention removal (@username)
- Hashtag symbol stripping
- Emoji conversion to text (🔥 → :fire:)
- Slang replacement
- Repeated character normalization
- Whitespace cleanup

This preprocessing ensures cleaner input for sentiment scoring.

---

### 2️⃣ NLTK – VADER Sentiment Analyzer

We use:


VADER (Valence Aware Dictionary and sEntiment Reasoner) is specifically designed for:

- Social media text
- Informal language
- Emphasis handling
- Capitalization intensity
- Punctuation strength

VADER outputs:

- Positive score
- Negative score
- Neutral score
- Compound score (overall sentiment)

Classification logic:

- Compound ≥ 0.05 → Positive  
- Compound ≤ -0.05 → Negative  
- Otherwise → Neutral  

---

### 3️⃣ Emoji Handling

We use:


This converts emojis into text form before sentiment scoring.

Example:
🔥 → :fire:
😡 → :angry_face:
😂 → :face_with_tears_of_joy:


This significantly improves interpretation of emotional signals.

---

### 4️⃣ Slang Normalization

Custom slang dictionary is applied:

```python
slang_dict = {
    "lit": "amazing",
    "bruh": "disappointed",
    "mid": "average",
    "fire": "excellent",
    "wtf": "angry",
    "omg": "surprised"
}

5️⃣ Character Normalization

Repeated characters are normalized:

soooo → soo
cooool → cool


This prevents exaggerated spellings from confusing the model.

🔬 Model Architecture
User Input
    ↓
Preprocessing Pipeline
    ↓
VADER Sentiment Analyzer
    ↓
Compound Score Calculation
    ↓
Sentiment Classification
    ↓
JSON Response

🛠 Tech Stack
Backend

FastAPI

Python 3.12

NLTK

Emoji

Frontend

HTML

CSS

JavaScript

Twitter-inspired layout

📁 Project Structure
Twitter_Sentiment_AI/
│
├── app.py
├── sentiment_model.py
├── templates/
│     └── index.html
├── static/
│     ├── style.css
│     └── script.js
├── venv/
└── README.md

🧪 Example Inputs
Input	Output
"This movie is sooo lit 🔥🔥"	Positive
"Bruh this is mid 😒"	Neutral
"WTF this is terrible 😡"	Negative

🎓 Learning Outcomes

Through this project, the following NLP concepts were applied:

Text normalization

Feature engineering

Sentiment lexicon usage

Rule-based sentiment scoring

API-based NLP deployment

Social media text processing

▶ How To Run

Create virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install fastapi uvicorn nltk emoji jinja2 python-multipart


Download VADER lexicon:

python
import nltk
nltk.download('vader_lexicon')
exit()


Run server:

uvicorn app:app --reload


Open browser:

http://127.0.0.1:8000

Deployed Live at : https://twitter-sentiment-ai.onrender.com
© Mobashshar Faiz
