import requests

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def generate_summary(description):
    prompt = f"Summarize this book in 2-3 lines:\n{description}"

    data = {
        "model": "mistral",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=data)
        result = response.json()
        return result['choices'][0]['message']['content']
    except:
        return "AI service not available"
    
def classify_genre(text):
    prompt = f"Classify the genre of this book:\n{text}"

    return generate_summary(prompt)


def analyze_sentiment(text):
    prompt = f"Analyze sentiment (Positive/Negative/Neutral):\n{text}"

    return generate_summary(prompt)    