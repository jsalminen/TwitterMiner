from slistener import SListener
import time, tweepy, sys

## auth. 
## TK: Edit the username and password fields to authenticate from Twitter.
#username = ''
#password = ''
#auth     = tweepy.auth.BasicAuthHandler(username, password)



## Eventually you'll need to use OAuth. Here's the code for it here.
## You can learn more about OAuth here: https://dev.twitter.com/docs/auth/oauth
consumer_key        = "itKIunsw8KmBXzN8DUigsX0x4"
consumer_secret     = "b0lBO3agrPKaG0pgjqXcEDtcWtCaLHaA1adQar4xO7wVHskLGY"
access_token        = "43863020-rizqB3it1yRJqVZ2fbjhMScBb4FNWXd8JIOF6r5fI"
access_token_secret = "LlPwCyzMSg2a78utR9BE7PgmOeQV9jEdGkICAoJUv3MAL"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api      = tweepy.API(auth)

def main( mode = 1 ):
    track  = ['problem', 'Problem']
    follow = []
            
    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print("Streaming started on %s keywords and %s users..." % (len(track), len(follow)))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()