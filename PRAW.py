import praw
import pandas as pd


reddit = praw.Reddit(
    client_id="O7ROFNDyYMuErA",
    client_secret="8W77vXPl2bHiossycbVvhMFMlC2iAQ",
    password="123Blizzard",
    user_agent="Custom web script by u/TheCanOpenerPodcast",
    username="TheCanOpenerPodcast",
)

print(reddit.user.me())

# get 100 top posts this week from the personalfinanceCanada subreddit
posts = []
CanInvestor = reddit.subreddit('CanadianInvestor')
for post in CanInvestor.top(time_filter='week', limit=1000):
    posts.append([post.title])
posts = pd.DataFrame(posts, columns=['title'])

newposts=posts["title"].str.split(" ")
print(newposts)




newposts.to_csv(r'/Users/Evan/Desktop/CanInvestorTopPost.csv', index = False)


# get 100 top posts this week from the personalfinanceCanada subreddit
#posts = []
#pfc_subreddit = reddit.subreddit('personalfinanceCanada')
#for post in pfc_subreddit.top(time_filter='week', limit=100):
#    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
#posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
#print(posts)

#posts.to_csv(r'/Users/Evan/Desktop/MLPoststest.csv', index = False)
