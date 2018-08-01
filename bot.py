# bot.py

import tweepy
import time
import threading
from threading import Thread
from database import *
from secrets import *
from RedditImport import grab_posts,grab_random
#create an OAuthHandler instance
# twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret);

api = tweepy.API(auth)

#public_tweets = api.home_timeline()

#for tweet in public_tweets:
#	print(tweet.text)


minutes = 1
minutesDirect = 1
subreddits = "me_irl"
directUsers = "@HGrimm21"




print("hello!\n\n")
#twt = api.search(q="Hello World!")

#api.send_direct_message(user="@murillians_tho", text="hello there")


def TimedMessage(message, times):
	temp = int(times)
	time.sleep(temp)
	s = api.update_status(message)

def UpdateDB(Subreddit,Postcount):
	posts=grab_posts(Subreddit,Postcount)
	for x in posts:
		addrpost(x.title,x.url,Subreddit)


test = "@"
counter = 0
StayLoop = 0
while StayLoop == 0:
	userChoice = 0
	print("MENU CHOICE 1:  TWEET")
	print("MENU CHOICE 2:  DIRECT MESSAGE")
	print("MENU CHOICE 3:  SCHEDULE POST")
	print("MENU CHOICE 4:  DAILY POST PREFERENCES")
	print("MENU CHOICE 5:  EXIT\n")
	userChoice = input("NUM: ")
	if userChoice == 1:
		message = raw_input("Type the message: ")
		s = api.update_status(message)
		print("Sent!\n")

	if userChoice == 2:
		userName = raw_input("Who do you want to direct message? (Example: @realDonaldTrump): ")
		message = raw_input("Type the message: ")
		api.send_direct_message(user= userName, text=message)

	if userChoice == 3:
		timeFromNow = input("Type how many minutes from now you want to post the message: ")
		timeFromNow = timeFromNow * 60
		randORnot = input("Do you want to type the message or pull one at random from a subreddit? (1 for message, 2 for random)")
		if randORnot == 1:
			message = raw_input("Type the message: ")
			tup = (message, timeFromNow)
			Thread(target = TimedMessage, args = tup).start()
		
			
		if randORnot == 2:
			post = getrpost('programming')
			print("Title is:")
			print(post[0])
			print("Link is:")
			print(post[1])
			message = post[0] + " " + post[1]
			tup = (message, timeFromNow)
			Thread(target =TimedMessage, args = tup).start()
			

	
	if userChoice == 4:
		print("POST EVERY (%i) MINUTES" %minutes)
		print("SEND DIRECT MESSAGES EVERY (%i) MINUTES" %minutesDirect)
		print("CHOOSE RANDOMLY FROM THESE SUBREDDITS: %s" %subreddits)
		print("SEND POSTS TO THESE USERS: %s\n\n" %directUsers)

		UpdatedPref = input("Do you want to update these preferences? (1 for yes,  2 for no): ")
		if UpdatedPref == 1:
			loopPref = 0
			while loopPref == 0:
				print("CHOICE 1:  UPDATE POST TIME")
				print("CHOICE 2:  UPDATE DIRECT MESSAGE TIME")
				print("CHOICE 3:  ADD SUBREDDITS")
				print("CHOICE 4:  REMOVE SUBREDDITS")
				print("CHOICE 5:  ADD USERS")
				print("CHOICE 6:  REMOVE USERS")

	if userChoice == 5:
		StayLoop = 1

print("\ntwitter bot updated 7.29.2018")

		
