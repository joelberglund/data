import twitter
import os
from dotenv import load_dotenv
load_dotenv()

apiKey = os.getenv('apiKey')
apiSecretKey = os.getenv('apiSecretKey')
accessToken = os.getenv('accessToken')
accessTokenSecret = os.getenv('accessTokenSecret')

api = twitter.Api(consumer_key=apiKey,consumer_secret=apiSecretKey,access_token_key=accessToken,access_token_secret=accessTokenSecret)

print(api.VerifyCredentials())

stream = api.GetStreamFilter(track=["@SwedishPM"])
for tweet in stream:
    print(tweet)

'''
GetStreamFilter(follow=None, track=None, locations=None, languages=None, delimited=None, stall_warnings=None, filter_level=None)[source]
Returns a filtered view of public statuses.

Parameters:	
follow – A list of user IDs to track. [Optional]
track – A list of expressions to track. [Optional]
locations – A list of Longitude,Latitude pairs (as strings) specifying bounding boxes for the tweets’ origin. [Optional]
delimited – Specifies a message length. [Optional]
stall_warnings – Set to True to have Twitter deliver stall warnings. [Optional]
languages – A list of Languages. Will only return Tweets that have been detected as being written in the specified languages. [Optional]
filter_level – Specifies level of filtering applied to stream. Set to None, ‘low’ or ‘medium’. [Optional]
'''
    