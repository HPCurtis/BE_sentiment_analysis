   # Saving Bachata Exchange

The following work is a personal project I created using my skills in Natural Language Processing (NLP) to help a campaign aimed at saving one of my favorite local dance events called Bachata Exchange in London. My contribution involved using NLP methods to collate and express the positive value of the event, as evidenced by the overwhelmingly positive reviews from its patrons.

## File structure

- BE_sentiment_analysis
   - README.md: The file your reading.
   - descriptive.py: analysis file to calcuate descritive of sentiment analyses
   - transformer.py: sentiment analysis pipeline using the transformer api and the distilbert-base-uncased-finetuned-sst-2-english pretrained model.
   - vader_scores.py: sentiment anlaysis using Vader scores
   - vis.py: file to produce analysis visualisations.
- data
   - reviews.csv: CSV file of TripAdvsior review scraped from scrapeHero Cloud.
   - tranformers_analysis_result.csv updated CSV from the reviews.csv file with the distilbert-base-uncased-finetuned-sst-2-english sentiment analysis results.
   - vader_analysis_results.csv: updated CSV from the reviews.csv file with the vader score sentiment analysis results.
- vis
   - word_cloud.png  

The first step of the project was to scrape the data from tripadvisor. To do this I used a service called [scrapeHero CLoud](https://cloud.scrapehero.com/crawlers) to scrape the reviews from Bachata exchanges associated tripadvisor page [see](https://www.tripadvisor.co.uk/Attraction_Review-g186338-d26663269-Reviews-Bachata_Exchange-London_England.html).

![wordcloud](vis/word_cloud.png)
Fig 1: Wordcloud generated on the non-event (removal of reference to location or day) specific words.

### Success
Overall the efforts invested by the various indivduals to save Bachata Exchagne were succesful with its return to London dance scene confirmed.