import tweepy 
import pandas as pd
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from sys import argv
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "********************************" 
consumer_secret = "********************************"
access_key = "********************************"
access_secret = "********************************"
  

          
# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# Access to user's access key and access secret 
auth.set_access_token(access_key, access_secret) 
  
# Calling api 
api = tweepy.API(auth) 



def tweet(handle, *args):

    tweets = []
    print('*************Fetching latest tweets*************')
    for status in tweepy.Cursor(api.user_timeline, screen_name=handle, tweet_mode="extended").items():
        tweets.append(status.full_text)

    df = pd.DataFrame(tweets, columns=['col'])

    df.to_csv('tweets.csv', index=None)
    print('**************CSV file saved in current working directory**************')

    stop_words = ['RT', 'https'] + list(STOPWORDS)


    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        background_color = 'black',
        stopwords = stop_words).generate(str(df['col']))
    fig = plt.figure(
        figsize = (40, 30),
        facecolor = 'k',
        edgecolor = 'k')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    fig.savefig('tweet_wordcloud.jpeg')
    print('**************Wordcloud image saved in current working directory**************')
 
 
 
tweet(*argv[1:])