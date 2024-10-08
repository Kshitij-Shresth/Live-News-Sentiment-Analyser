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

def plot_ring_chart(sentiments):
    sizes = [sentiments['positive'], sentiments['neutral'], sentiments['negative']]
    labels = ['Positive', 'Neutral', 'Negative']
    colors = ['#4caf50', '#ffeb3b', '#f44336']

    fig, ax = plt.subplots()
    wedges, _, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                  startangle=90, wedgeprops=dict(width=0.3))
plt.setp(autotexts, size=10, weight="bold")
plt.title('Sentiment Analysis Ring Chart')

img = io.BytesIO()
plt.savefig(img, format='png')
img.seek(0)
plt.close()

return img
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        sentiments = analyze_sentiment(query)
        img = plot_ring_chart(sentiments)

        return send_file(img, mimetype='image/png', as_attachment=False, download_name='chart.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
