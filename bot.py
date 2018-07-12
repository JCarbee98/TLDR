# NOTE FOR OTHER PEOPLE!!!!!
# THIS IS MISSING IMPORTS FROM Tweeby so make sure to import it!
# It is also missing Secrets.Py which has private keys that should not be public!


# bot.py

import tweepy
import time
from secrets import *

#create an OAuthHandler instance
# twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()

#for tweet in public_tweets:
#	print(tweet.text)


print("hello!\n\n")
#twt = api.search(q="Hello World!")

#api.send_direct_message(user="@murillians_tho", text="hello there")
test = "@"
counter = 0
StayLoop = 0
while StayLoop == 0:
	userChoice = 0
	print("MENU CHOICE 1:  TWEET")
	print("MENU CHOICE 2:  EXIT")
	userChoice = input("NUM:")
	if userChoice == 1:
		message = raw_input("Type the message: ")
		s = api.update_status(message)
	if userChoice == 2:
		StayLoop = 1

print("\ntwitter bot updated 7.11.2018")

		
