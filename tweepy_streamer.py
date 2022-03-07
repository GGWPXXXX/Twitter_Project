from logging.config import listen
from tweepy.streaming import StreamingClient
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class TwiiterStreamer():
    def stream_tweets(self, fetched_tweets_filename ,hashtag_list):
    #Handle Twiiter Authentication and the connection to the twitter API
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    
    stream = Stream(auth, listener)
    stream.filter(track=hash_tag_list)
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)
        
        
if __name__== "__main__":
    listener = StdOutListener()
    auth=OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS TOKEN, twitter credentials.ACCESS_TOKEN_SECRET)
    
    stream = Stream(auth, listener)
    
    stream.filter(track=['STAR WARS','Kylo Ren','Darth Vader'])