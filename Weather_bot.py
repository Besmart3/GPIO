# import tweepy
# import pyowm
# import schedule
# import time

# # Replace with your actual Twitter API keys and tokens
# twitter_auth = tweepy.OAuth1UserHandler(
#     '8ESLbeCw2NVwnK5mZVUFDUzXE',
#     'JewcURYB629uahsH3G5U08Vvx5tO8fTyjTB5KmTcuUyuKGGKfc',
#     '1826614476843397120-rElByonbRCYwT3nvejeyDQv2WoyJUj',
#     'QtQItrYHRsnUsU8zo4h9JxU6EJssXuKlCUVGlidavNvGr'
# )

# # Initialize the Twitter API client
# twitter_api = tweepy.API(twitter_auth)

# # Replace with your OpenWeatherMap API key
# owm_api_key = '02b1d494b33aa0f642aa34529e1680ac'
# owm = pyowm.OWM(owm_api_key)

# # Function to get weather emojis based on weather description
# def get_weather_emojis(weather_description):
#     emojis = {
#         'clear sky': '☀️',
#         'few clouds': '🌤️',
#         'scattered clouds': '⛅',
#         'broken clouds': '☁️',
#         'shower rain': '🌦️',
#         'rain': '🌧️',
#         'thunderstorm': '⛈️',
#         'snow': '❄️',
#         'mist': '🌫️'
#     }
#     for key in emojis:
#         if key in weather_description.lower():
#             return emojis[key]
#     return '🌎'

# # Function to tweet the weather
# def tweet_weather():
#     observation = owm.weather_at_place('London,GB')  # Change to your preferred location
#     weather = observation.get_weather()
#     weather_description = weather.get_detailed_status()
#     weather_emojis = get_weather_emojis(weather_description)
#     tweet_text = f"The weather in London is: {weather_description} {weather_emojis}"
    
#     # Post the tweet
#     twitter_api.update_status(tweet_text)
#     print(f"Tweeted: {tweet_text}")

# # Schedule the tweet every hour
# schedule.every().hour.do(tweet_weather)

# # Keep the bot running
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import tweepy
import pyowm
import schedule
import time

# Replace with your actual Twitter API keys and tokens
twitter_auth = tweepy.OAuth1UserHandler(
    '8ESLbeCw2NVwnK5mZVUFDUzXE',
    'JewcURYB629uahsH3G5U08Vvx5tO8fTyjTB5KmTcuUyuKGGKfc',
    '1826614476843397120-rElByonbRCYwT3nvejeyDQv2WoyJUj',
    'QtQItrYHRsnUsU8zo4h9JxU6EJssXuKlCUVGlidavNvGr'
)

# Initialize the Twitter API client
twitter_api = tweepy.API(twitter_auth)

# Replace with your OpenWeatherMap API key
owm_api_key = '02b1d494b33aa0f642aa34529e1680ac'
owm = pyowm.OWM(owm_api_key)

# Function to get weather emojis based on weather description
def get_weather_emojis(weather_description):
    emojis = {
        'clear sky': '☀️',
        'few clouds': '🌤️',
        'scattered clouds': '⛅',
        'broken clouds': '☁️',
        'shower rain': '🌦️',
        'rain': '🌧️',
        'thunderstorm': '⛈️',
        'snow': '❄️',
        'mist': '🌫️'
    }
    for key in emojis:
        if key in weather_description.lower():
            return emojis[key]
    return '🌎'

# Function to tweet the weather
def tweet_weather():
    observation = owm.weather_at_place('London,GB')  # Change to your preferred location
    weather = observation.get_weather()
    weather_description = weather.get_detailed_status()
    weather_emojis = get_weather_emojis(weather_description)
    tweet_text = f"The weather in London is: {weather_description} {weather_emojis}"
    
    # Post the tweet
    twitter_api.update_status(tweet_text)
    print(f"Tweeted: {tweet_text}")

# Schedule the tweet every hour
schedule.every().hour.do(tweet_weather)

# Keep the bot running
while True:
    schedule.run_pending()
    time.sleep(1)