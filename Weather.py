# import pyowm

# owm = pyowm.OWM('2c83d04e1ca424fe141b7689aa9a632c') 
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('London,uk')
# w = observation.weather



# # w.wind()
# # w.humidity()
# print(w.status, w.humidity, w.wind())

# import pyowm

# # Initialize the OWM object with your API key
# owm = pyowm.OWM('3b06764349f3643799723c2b9b7e7127') 

# # Get the weather manager
# mgr = owm.weather_manager()

# # Get weather observation for a place
# observation = mgr.weather_at_place('Accra,Ghana')

# # Get the weather object
# w = observation.weather

# # Print weather status, humidity, and wind information
# print(w.status,w.humidity, w.wind())


# from pprint import pprint
# import requests
# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=deb72ae973c30cd63bacd8907d246a4f')
# pprint(r.json()) 
# import tweepy

# auth = tweepy.Client(
#     'zY2nHGMvpcfyBg9h7LrE9aPAv', 
#     'XFttTVny7Z8Bryfo8BwR027tzV4Jp9Aj5RyEyGIzyr0hmAo2CU', 
#     '1826614476843397120-abWNOQ7IpMmj8XxjnJzOTleW4wuO4f', 
#     'kcEreznQyg7XCCDuxUHOF8D6gqqyqHKmmHIjzTZyL60V1'
# )

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

import tweepy

# Initialize the client with your API keys and tokens
client = tweepy.Client(
    consumer_key="TvYPCMy5hTI65a1flXAZAbGrS",
    consumer_secret="FJt13qVDXjs1evqPg0T90fg2uJqBncP3mLG6JtOzVhYMqlkT6G",
    access_token="1826614476843397120-k9shSX6AohHiEbL8GEUJvzAn69suWU",
    access_token_secret="QODkz7L8naCQkO748EcCp0X0hJdLOnEtwQ0bRSviK168V"
)

# Create and send a tweet
response = client.create_tweet(text='Hello, world! This is my first tweet using Twitter API v2!')

# Check if the tweet was successfully created
if response.data:
    print(f"Tweet sent successfully: {response.data['text']}")
else:
    print("Failed to send tweet.")
