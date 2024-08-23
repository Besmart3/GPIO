# import pyowm

# owm = pyowm.OWM('2c83d04e1ca424fe141b7689aa9a632c') 
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('London,uk')
# w = observation.weather



# # w.wind()
# # w.humidity()
# print(w.status, w.humidity, w.wind())

import pyowm

# Initialize the OWM object with your API key
owm = pyowm.OWM('2c83d04e1ca424fe141b7689aa9a632c') 

# Get the weather manager
mgr = owm.weather_manager()

# Get weather observation for a place
observation = mgr.weather_at_place('London,uk')

# Get the weather object
w = observation.weather

# Print weather status, humidity, and wind information
print(w.status, w.humidity, w.wind())
