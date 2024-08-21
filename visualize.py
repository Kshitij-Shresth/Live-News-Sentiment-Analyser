#Function to plot a ring chart
def plot_ring_chart(sentiments):
    sizes = [sentiments['positive'], sentiments['neutral'], sentiments['negative']]
    labels = ['Positive', 'Neutral', 'Negative']
    
    #Define colors for the ring chart
    colors = ['#4caf50', '#ffeb3b', '#f44336']
    
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                      startangle=90, wedgeprops=dict(width=0.3))
    ax.legend(wedges, labels,
              title="Sentiment",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
#setting the legend
    
    plt.setp(autotexts, size=10, weight="bold")
    plt.title('Sentiment Analysis Ring Chart')
    plt.show()

query = input("Enter the subject to analyze: ")
result, articles = analyze_sentiment(query)
print(f"Sentiment Analysis for {query}:")
print(f"Positive: {result['positive']}")
print(f"Neutral: {result['neutral']}")
print(f"Negative: {result['negative']}")
plot_ring_chart(result)
