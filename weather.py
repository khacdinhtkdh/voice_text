# import the module
import python_weather
import asyncio
from main import speak

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find('Hanoi')

    # returns the current day's forecast temperature (int)

    print(weather.current.temperature)
    speak(f'temperature is {weather.current.temperature}')
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        speak(str(forecast.date))
        speak(forecast.sky_text)
        speak(str(forecast.temperature))

    # close the wrapper once done
    await client.close()