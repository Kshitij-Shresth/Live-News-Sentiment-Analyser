def analyze_sentiment(query, max_articles=50):
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'en',
        'pageSize': max_articles
    }
    
