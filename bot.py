from tweepy.auth import OAuthHandler
from keys import *
import tweepy
import time
import random, os



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def openRndDir():
    
    dir = os.getcwd()
    files = os.listdir(dir) 
    random_file = random.choice(files)
    return open(random_file, "r", encoding="utf8")


def getRndQuote (file):
    quote = file.read()
    line = random.randrange(1, quote.count('$')+1, 1)
    quote = quote.split('$')[line][:-2]
    file.close()
    return quote

#   Get Quote Function
#       @output: string of the selected quote
def getQuote():
    return getRndQuote(openRndDir())


def main():
    os.chdir("lyrics")
    
    while True:
        quote = getQuote()
        
        try:
            api.update_status(quote) 
            print (quote)
            time.sleep(14400)   

            
        except tweepy.TweepError:
             api.update_status(quote) 
             print (quote)
             time.sleep(14400)   

            
        
        
        
    
if __name__== "__main__":
    main()
