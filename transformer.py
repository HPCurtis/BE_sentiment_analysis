from transformers import pipeline
import pandas as pd

# Genearete pipeline as global this has to be done 
# so the pipline is only called once and speeds up
# dramatically. 
sentinment_pipe = pipeline("sentiment-analysis")

def main():
    # Laod tripadvisor data into pandas dataframes. 
    df = pd.read_csv("data/reviews.csv")

    # Apply calculate_vader_scores and stor the reuslts in seperate columns 
    df['sentiment_scores'] = df['reviewBody'].apply(sentiment_analysis).apply(pd.Series)

    # Save out results.
    df.to_csv('data/tranformers_analysis_results.csv', index=False)

def sentiment_analysis(text):
    # Create the sentiment analysis pipeline.
    return(sentinment_pipe(text))

if __name__ == "__main__":
    main()