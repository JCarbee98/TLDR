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


f = file("Preferences.txt", 'r+')

subreddits = []
directUsers = []



minutes = f.readline()
minutesDirect = f.readline()
loopTime = int(f.readline())
for x in range(loopTime):
	temp = f.readline()
	temp = temp.rstrip('\n')
	subreddits.append(temp)

loopTime = int(f.readline())

for x in range(loopTime):
	temp = f.readline()
	temp = temp.rstrip('\n')
	directUsers.append(temp)


<<<<<<< HEAD
print("hello!\n\n")
=======
f.close()


print("Welcome to our bot!")
>>>>>>> 7e4a5e88f35eb0d3e65086cef86e779d8b19e5b9
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


#def RunPreferences():






test = "@"
counter = 0
StayLoop = 0
while StayLoop == 0:
	userChoice = 0
	print("\n************************")
	print("MENU CHOICE 1:  TWEET")
	print("MENU CHOICE 2:  DIRECT MESSAGE")
	print("MENU CHOICE 3:  SCHEDULE POST")
	print("MENU CHOICE 4:  DAILY POST PREFERENCES")
	print("MENU CHOICE 5:  EXIT\n")
	userChoice = input("NUM: ")
	print("************************")
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
		print("POST EVERY (%i) MINUTES" %int(minutes))
		print("SEND DIRECT MESSAGES EVERY (%i) MINUTES" %int(minutesDirect))
		print("CHOOSE RANDOMLY FROM THESE SUBREDDITS: %s" %subreddits)
		print("SEND POSTS TO THESE USERS: %s\n" %directUsers)

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
				print("CHOICE 7:  BACK TO MENU")
				
				WhichPref = input("NUM: ")

				if WhichPref == 1:
					minutes = input("Enter a number to post ever X minutes: ")
				if WhichPref == 2:
					minutesDirect = input("Enter a number to direct message every X minutes: ")
				if WhichPref == 3:
					print("Current subreddit list is: ", subreddits)
					NewSubreddit = raw_input("Type the name of the new subreddit (EX: me_irl): ")
					subreddits.append(NewSubreddit)
				if WhichPref == 4:
					print("Current subreddit list is: ", subreddits)
					RemoveSubreddit = raw_input("Type the name of the subreddit you want to remove (EX: me_irl): ")
					subreddits.remove(RemoveSubreddit)
				if WhichPref == 5:
					print("Current user list is: ", directUsers)
					NewUser = raw_input("Type the name of the new user: ")
					directUsers.append(NewUser)
				if WhichPref == 6:
					print("Current user list is: ", directUsers)
					RemoveUser = raw_input("Type the name of the user to delete: ")
					directUsers.remove(RemoveUser)					
				if WhichPref == 7:
					print("If you made changes to the preferences restart the program for them to take effect!")
					f = file("Preferences.txt", 'w')
					f.write(str(minutes))
					f.write("\n")
					f.write(str(minutesDirect))
					f.write("\n")
					f.write(str(len(subreddits)))
					f.write("\n")
					for x in range(0 ,len(subreddits)):
						f.write(subreddits[x])
						f.write("\n")

					f.write(str(len(directUsers)))
					f.write("\n")
					for x in range(0, len(directUsers)):
						f.write(directUsers[x])
						f.write("\n")
					f.close()

					
					loopPref = 1

	if userChoice == 5:
		StayLoop = 1

print("\ntwitter bot updated 8.1.2018")

		
