"""
Author: Harrison Curtis
"""

# Import packages and dowload the required lexicon for the following analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import download
download('vader_lexicon')
import pandas as pd 

sia = SentimentIntensityAnalyzer()

# Functions for vader sentinent analysis.
def calculate_vader_scores(text):
    # Geneate SIA scores
    return sia.polarity_scores(text)

def main():
    # Laod tripadvisor data into pandas dataframes. 
    df = pd.read_csv("data/reviews.csv")

    # Apply calculate_vader_scores and stor the reuslts in seperate columns 
    df[['neg', 'neu', 'pos', 'compound']] = df['reviewBody'].apply(calculate_vader_scores).apply(pd.Series)

    # Save out results.
    df.to_csv('data/vader_analysis_results.csv', index=False)

if __name__ == "__main__":
    main()