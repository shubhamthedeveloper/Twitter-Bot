# This is the twitter bot which uses the tweepy library 
# This bot can like the posts which matches the search string 
# It can also follow back all your followers and much more.
# More options and functions can be explored on the Tweepy docs.
import tweepy
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.me()

# so that we dont hit the twitter server again and again 
def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)



#  /*** like the tweets with search string ***/
search_string = 'python'
NumberOfTweets =2;

for tweets in tweepy.Cursor(api.search,search_string).items(NumberOfTweets):
	try:
		tweets.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break;


# /*** bot that can follow back all your followers ***/
# for follower in tweepy.Cursor(api.followers).items():
	# to follow some specific person 
	# if follower.name() == '':
	# 	follower.follow()
	# 	break

	# to follow everyone 
	# follower.follow()
	
	# to print all the people who follows you 
	# print(follower.name())



