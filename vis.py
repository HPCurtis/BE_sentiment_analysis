import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from descriptives import sentiment_split

# Run programme to produce visualisation for analyses of reviews. 
def main():

    # Read in the analysis results for descritive analyses.
    transformer_df = sentiment_split(pd.read_csv("data/tranformers_analysis_results.csv"))
    print(transformer_df)
    transformer_df['reviewRating'] = transformer_df['reviewRating'].astype("string").str.rstrip('.').astype(float).astype(int)
    
    vader_df = pd.read_csv("data/vader_analysis_results.csv")

    # Generate wordcloud.
    wordcloudvis(transformer_df, review_col="reviewBody")
    # Plot star ratings
    star_bar_plot(transformer_df, col="reviewRating")

    # Plot transformer scores
    hist_plot(transformer_df)

def star_bar_plot(df, col):
    """
        Produce bar plot of the review ratings.
    """
    # COnvert to categorical value.
    df[col] = df[col].astype('category')

    # Calcvaute the number of reviews in each category.
    star_groups = df.groupby(col).size().reset_index(name='counts')

    # Plotting
    fig, ax = plt.subplots()
    bars = ax.bar(star_groups[col], star_groups['counts'], color='skyblue')

    # Adding counts on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # va='bottom' ensures the text is above the bar

    plt.xlabel("Rating")
    plt.ylabel('Count')
    plt.title(f'Number of each star rating')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.savefig('vis/starbar.png', format='png', dpi=300)

def wordcloudvis(df, review_col):
    """
        Produce word cloud plot from pandas series.
    """
    # Combine all text entries into a single string
    text = " ".join(review for review in df[review_col])

    # Words to remove
    uncessary_words  = ["Bachata", "London", "London!", "London.",  "London,", "LONDON", 
                        "LONDON.", "Londoners", "London's", "London!The", "london"
                        "bachata", "Exchange", "exchange", "exchange.", "Exchange", 
                         "dance", "dance.", "dancing", "dancers", "dancers!"
                        "dancing.", "dancer", "dancer!", "Sunday"]
    
    # Remove those words from the text
    for word in uncessary_words:
        text = text.replace(f" {word} ", " ")

    # Create and display the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.axis("off")
    plt.imshow(wordcloud, interpolation="bilinear")
    # Save the wordcloud figure out 
    plt.savefig('vis/word_cloud.png', format='png', dpi=300)

def hist_plot(df):
    #print(df["score"])
    fig, ax = plt.subplots()
    ax.hist(df["score"])
    plt.xlabel("Sentiment score")
    plt.title(f'Sentient analysis score for postively classified reviews')
    plt.ylabel('Count')
    plt.savefig('vis/transformer_scores.png', format='png', dpi=300)
    
   
    #plt.savefig('vis/transformer_scores.png', format='png', dpi=300)

if __name__ == "__main__":
    main()