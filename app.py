app = Flask(__name__)
api_key = ''
endpoint = ''

def analyze_sentiment(query, max_articles=50):
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'en',
        'pageSize': max_articles
    }
response = requests.get(endpoint, params=params)
    data = response.json()

    articles = data.get('articles', [])
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}

    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        text = f"{title} {description}"

        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1
        else:
            sentiments['negative'] += 1

    return sentiments
