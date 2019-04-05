from twython import TwythonStreamer,Twython
import csv
import os
import sys
import twython
from pprint import pprint as pp
import time
# Filter out unwanted data
def process_tweet(tweet,self):
    pp(tweet)
    d['likes'] = tweet['favorite_count']
    d['retweets_num'] = tweet['retweet_count']
    d['relationship'] = tweet['retweet_status']
    
    d['user'] = tweet['user']['screen_name']
    #d['user_loc'] = tweet['user']['location']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        try:
            if data['lang'] == 'en':
                twitter = Twython('x4FguSwehXpgdPtq2bTi5dOJU', 'yAHfjLyxuct4I6He9uDbqr547MN0RP6ghdSFgYn19XDF4uXbge', '2219948304-c60sVwWulIqRJLnPSFH6rMWn9uMIvYxmQSTQx56','dH11u0vsbWIiMBzgEbHTgpFSzlrmu0vhyGfqbXiRsBsUf')
                if data['favorite_count'] > 10:
                    tweet_data = process_tweet(data,twitter)
                    self.save_to_csv(tweet_data)
        except data['lang'] != 'en':
            pass

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

def update(stream1):
    period = time.time() +60*60 #set the period to be one hour
    while(time.time() < period):
        pass

    stream.statuses.filter(track = 'president')



if __name__ == "__main__":
    stream1 = MyStreamer('x4FguSwehXpgdPtq2bTi5dOJU', 'yAHfjLyxuct4I6He9uDbqr547MN0RP6ghdSFgYn19XDF4uXbge', '2219948304-c60sVwWulIqRJLnPSFH6rMWn9uMIvYxmQSTQx56','dH11u0vsbWIiMBzgEbHTgpFSzlrmu0vhyGfqbXiRsBsUf')
    stream1.statuses.filter(track = 'president')
    #update(stream1)
