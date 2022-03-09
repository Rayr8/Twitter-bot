# import packages
import pip
import tweepy
import time

# Authenticate to twitter

consumer_key = 'f99uPFwpun7pUMhq0joCYV0dO'
consumer_secret = 'ZzfoJm5mBSkNvHwFIUPGGrE3sW26YTS0R7JprikcKqN7loRXTk'
access_key = '1418185296726855681-Vc5yTMa6rUesnsACFoeuUkE4kt2HZM'
access_secret = '9xGt9e9hvMCzw16uaDqYX5TiJJuOtcuoTIrZn5KE5kHWe'

# Create API object

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'fashion'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:

        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
