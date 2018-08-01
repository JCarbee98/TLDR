import praw

'''

PRAW is a Reddit interface object that allows the scraping of posts from subreddits.

To use grab_posts in it's current state, pass a list of subreddits, a list of numerical arguments for which posts to
grab, and an optional amount of posts to grab (defaults to one post). The function will scrape the desired posts from
Reddit and return a list containing lists (the actual posts) which hold the post's
title, score, and url. You can then parse this returned structure to display the information or send it over twitter.

'''

# don't change this, it's specific to the bot reddit account I made
red = praw.Reddit(user_agent='windows:example.twitterredditbot:v.1 (by students)',
                  client_id='9aUOvaqOIkNprg',
                  client_secret='1DePUPByrds4R7lAk6xv1NyE1ww')


def grab_posts(subs, numposts=1): #default value, can be made larger for grabbing more posts
    info = []   #list to hold lists of info

    for sub in subs:    #for all the subs we need to go through
        for post in red.subreddit(sub).top('day', limit=numposts):
            pst = []  # list to hold singular post info

            pst.append(post.title)  #collect data
            pst.append(post.score)
            pst.append(post.url)

            info.append(pst)
    return info                     #return it

def grab_random():	#grabs the top post over a day from a random subreddit and returns it
	for post in red.random_subreddit().top('day', limit=1):
		pst = []

		pst.append(post.title)
		pst.append(post.score)
		pst.append(post.url)

		return pst


'''
This is just in here for testing, making sure that reddit is being scraped properly.

grab_posts will eventually just be called with a list of subreddit names gleaned
from the database of registered users.

If we are going to be having the bot post the hot links from the past 24 hours
publically, we will call grab_posts against a pre-chosen group of subs
'''


choice = ''
subreddits = []
post_types = []

print("Please enter subreddits you are interested in. When you are finished, type 'done'")
while True:
    choice = input()
    if choice == "done":
        break
    else:
        subreddits.append(choice)

number = int(input("Please enter the number of posts you want: "))

stuff = grab_posts(subreddits, number)
random = grab_random()

print(stuff)
print(random)
