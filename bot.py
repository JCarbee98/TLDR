# NOTE FOR OTHER PEOPLE!!!!!
# THIS IS MISSING IMPORTS FROM Tweeby so make sure to import it!
# It is also missing Secrets.Py which has private keys that should not be public!


# bot.py

import tweepy
import time
from secrets import *

# create an OAuthHandler instance
# twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


def limit_handled(cursor):  # code to wait 15 min when rate limited before trying again
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


for tweet in public_tweets:
    print(tweet.text)

print("hello!\n\n")
twt = api.search(q="Hello World!")
t = ['Hello world!', 'Hello World!', 'Hello World!!!', 'hello world!', 'Hello, World!']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
