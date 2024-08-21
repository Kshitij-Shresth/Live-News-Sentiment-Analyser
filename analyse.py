response = requests.get(endpoint, params=params)
data = response.json()
articles = data.get('articles', [])

#Holding sentiment analysis counts in a dictionary
sentiments = {'positive': 0, 'neutral': 0, 'negative': 0} 
   for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        text = f"{title} {description}"
     
#Combining the title and description to form the text for sentiment analysis
analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1
        else:
            sentiments['negative'] += 1
#Classifying the sentiment based on polarity to update sentiment counts
          
return sentiments, articles
