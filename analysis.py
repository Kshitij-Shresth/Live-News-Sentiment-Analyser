# Fetch news articles and perform sentiment analysis
def analyze_sentiment(query, max_articles=50):
    # Define the parameters for the API request
    params = {
        'q': query,  # The query parameter for the search term
        'apiKey': api_key,  # The API key for authentication
        'language': 'en',  # The language of the news articles
        'pageSize': max_articles  # The number of articles to fetch
    }
    
    # Make the API request to fetch news articles
    response = requests.get(endpoint, params=params)
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    #Extracting the articles from the response data
    articles = data.get('articles', []) 
    #Initializing a dictionary to hold sentiment counts
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for article in articles:  
       title = article.get('title', '')
      description = article.get('description', '')
    #Combining the title and description to form the text for sentiment analysis
      text = f"{title} {description}"
        analysis = TextBlob(text)
        
        #Classifying the sentiment based on polarity and updating the sentiment counts
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1 
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1  
        else:
            sentiments['negative'] += 1 
    return sentiments, articles
