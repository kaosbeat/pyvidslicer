import sys
import tweepy
from lib.tweetkeys import *



def tweetimg(image_path, text):
    print("invoking TWEEEEEETING")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)       
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    tweet = text
    # image_path = "tweet.png" # png created above
    print(image_path, text)
    file=open(image_path, 'rb')
    media_id = api.simple_upload(filename=image_path, file=file)
    print(media_id)
    api.update_status(tweet, media_ids=[media_id.media_id_string])


