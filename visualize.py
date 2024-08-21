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
