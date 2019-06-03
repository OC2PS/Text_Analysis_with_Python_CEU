

import os
os.chdir("/Users/ariedamuco/Dropbox (CEU Econ)/TextAnalysisCEU")
import pandas as pd # data processing

amazon=pd.read_csv('Input/Amazon_Unlocked_Mobile.csv')
#amazon=pd.read_csv('Input/Amazon_Unlocked_Mobile.csv',  nrows=1000)

amazon.head()
amazon_short=amazon[0:1000]

review=amazon[['Reviews']][0:1000]
review=review.dropna()
#import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()
#sentiment.polarity_scores("The phone is super cool.")
#sentiment.polarity_scores("The phone is super cool!")
#sentiment.polarity_scores("The phone is super cool!!")
#sentiment.polarity_scores("The phone is super cool!!!")
#sentiment.polarity_scores("The phone is super COOL")
#sentiment.polarity_scores("I am so happy :)")
"""
for sentences in review['Reviews']:
    s = sentiment.polarity_scores(sentences)
    for k in sorted(s):
        print('{0}: {1}, '.format(k, s[k]))
    print(sentences)
"""
#rev['polarity']=rev['Reviews'].apply(lambda x: sentiment.polarity_scores(str(x)))

review['polarity_score']=review['Reviews'].apply(lambda x: sentiment.polarity_scores(str(x))['compound'])

review['neutral'] = review['Reviews'].apply(lambda x:sentiment.polarity_scores(str(x))['neu'])
review['negative'] = review['Reviews'].apply(lambda x:sentiment.polarity_scores(str(x))['neg'])
review['positive'] = review['Reviews'].apply(lambda x:sentiment.polarity_scores(str(x))['pos'])


review['sentiment']=''
review.head()

review.loc[review.polarity_score>0,'sentiment']='Positive'
review.loc[review.polarity_score==0,'sentiment']='Neutral'
review.loc[review.polarity_score<0,'sentiment']='Negative'
review.head()
#import matplotlib.pyplot as plt


amazon_short[['polarity_score', 'sentiment']]=review[['polarity_score', 'sentiment']]

import seaborn as sns
sns.countplot(x='Rating', data=amazon_short, palette="Purples")
sns.countplot(x='sentiment', data=amazon_short, palette="Purples")
sns.countplot(x='Rating', hue="sentiment", data=amazon_short, palette="Purples")
