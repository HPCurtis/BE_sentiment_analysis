"""
Author: Harrison Curtis
"""
# Import neccary libraries.
import pandas as pd

def main():

    # Read in the analysis results for descritive n
    tranformer_df = pd.read_csv("data/tranformers_analysis_results.csv")
    vader_df = pd.read_csv("data/vader_analysis_results.csv")

    # Number of reviews
    n_reviews = len(tranformer_df)
    print(n_reviews)

    # Get the avaege length of reviews
    print(avg_review_length(tranformer_df, reviews_col="reviewBody"))


def count_words(text):
    # Split the string by whitespace and return the length of the resulting list
    return len(text.split())

def avg_review_length(df, reviews_col):

    """
        Function to clacute the average lenght of online review in pandas dataframe.

        Args:
            df (pandas.DataFrame): The DataFrame containing the text data.
            column_name (str): The name of the column containing the text data.

        returns: 
            int: of the avaerge review length in dataframe review_col.
    """
    # Get the length of eahc review.
    df['text_length'] = df[reviews_col].apply(count_words)

    # Round the answer to whole number.
    average_length = int(round(df['text_length'].mean(), 0))
    return(average_length)

if __name__ == "__main__":
    main()