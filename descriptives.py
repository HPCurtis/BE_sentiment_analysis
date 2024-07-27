"""
Author: Harrison Curtis
"""
# Import neccary libraries.
import pandas as pd
import ast

def main():

    # Read in the analysis results for descritive n
    tranformer_df = sentiment_split(pd.read_csv("data/tranformers_analysis_results.csv"))
    vader_df = pd.read_csv("data/vader_analysis_results.csv")

    # Get the avaege length of reviews
    print(avg_review_length(tranformer_df, reviews_col="reviewBody"))

    # Number of reviews
    n_reviews = len(tranformer_df)
    n_postive_reviews = sum(tranformer_df["label"] == "POSITIVE")
    print(n_reviews)
    print(n_postive_reviews)

    # Extract the negative review
    # Example of misclassficaiton from the model
    # with high score.
    negative_review = tranformer_df[tranformer_df["label"] == "NEGATIVE"]
    negative_review_body = negative_review["reviewBody"]
    negative_review_body.to_csv('data/negativereview.txt', sep=' ', index=False)
    print(negative_review["sentiment_scores"])

    

# Functions to count base descritive stats.
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

# Functions for transfromer model descriptives.

def convert_to_dict(string):
    return ast.literal_eval(string)

def sentiment_split(df , col = "sentiment_scores"):
    """
    """

   # Convert the 'sentiment_scores' column to dictionaries
    df[col] = df[col].apply(convert_to_dict)

    # Split the 'sentiment_scores' column into separate columns
    sentiment_scores_df = df[col].apply(pd.Series)

    # Concatenate the sentiment scores DataFrame with the original DataFrame
    df = pd.concat([df, sentiment_scores_df], axis=1)

    # Display the DataFrame
    return(df)


if __name__ == "__main__":
    main()