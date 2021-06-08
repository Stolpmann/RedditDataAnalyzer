from psaw import PushshiftAPI
import csv

api = PushshiftAPI()
gen = api.search_comments(subreddit='CanadianInvestor', limit=1000, after="7d")

with open('reddit_analysis.csv', 'w', newline='') as csvfile:
    writerobj = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for comment in gen:
        writerobj.writerow([comment.body])