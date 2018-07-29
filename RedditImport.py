import praw
from secrets import *
'''

PRAW is a Reddit interface object that allows the scraping of posts from subreddits.

To use grab_posts in it's current state, pass a list of subreddits, a list of numerical arguments for which posts to
grab, and an optional amount of posts to grab (defaults to one post). The function will scrape the desired posts from
Reddit and return a list of lists (the categories of posts) containing lists (the actual posts) which hold the post's
title, score, and url. You can then parse this returned structure to display the information or send it over twitter.

0 = top
1 = controversial
2 = hot
3 = gilded
4 = top post of the day from a random subreddit

'''

# don't change this, it's specific to the bot reddit account I made
'''
red = praw.Reddit(user_agent=ruser_agent,
                  client_id=rclient_id,
                  client_secret=rclient_id)##
'''
red = praw.Reddit(user_agent='windows:example.twitterredditbot:v.1 (by students)',
                  client_id='9aUOvaqOIkNprg',
                  client_secret='1DePUPByrds4R7lAk6xv1NyE1ww')
def grab_posts(subs, cats, numposts=1): #default value, can be made larger for public posting
    info = []   #list to hold lists of info

    for sub in subs:    #for all the subs we need to go through
        for num in cats:
            category = []  # container for posts from a certain category

            if num == 0:    #top
                for post in red.subreddit(sub).top('day', limit=numposts):
                    pst = []  # list to hold singular post info

                    pst.append(post.title)  #collect data
                    pst.append(post.score)
                    pst.append(post.url)

                    category.append(pst)        #append to category holder
                info.append(category)
            elif num == 1:
                for post in red.subreddit(sub).controversial('day', limit=numposts):
                    pst = []  # list to hold singular post info

                    pst.append(post.title)
                    pst.append(post.score)
                    pst.append(post.url)

                    category.append(pst)
                info.append(category)
            elif num == 2:
                for post in red.subreddit(sub).hot('day', limit=numposts):
                    pst = []  # list to hold singular post info

                    pst.append(post.title)
                    pst.append(post.score)
                    pst.append(post.url)

                    category.append(pst)
                info.append(category)
            elif num == 3:
                for post in red.subreddit(sub).gilded('day', limit=numposts):
                    pst = []  # list to hold singular post info

                    pst.append(post.title)
                    pst.append(post.score)
                    pst.append(post.url)

                    category.append(pst)
                info.append(category)
            elif num == 4:
                for post in red.random_subreddit().top('day', limit=numposts):
                    pst = [] # list to hold singular post info

                    pst.append(post.title)
                    pst.append(post.score)
                    pst.append(post.url)

                    category.append(pst)
                info.append(category)
    return info                     #return it



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
print("Please enter the types of posts you want: \n\n0 = top\n1 = controversial\n2 = hot\n3 = gilded\n4 = top from a random sub\n\n")
while True:
    choice = input()
    if choice == "done":
        break
    else:
        post_types.append(choice)

number = int(input("Please enter the number of posts you want: "))

stuff = grab_posts(subreddits, post_types, number)

print(subreddits)
print(post_types)
print(stuff)
