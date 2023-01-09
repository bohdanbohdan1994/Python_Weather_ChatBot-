import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather (city, open_weather_token ):

    code_to_smile = {
        "Clear": "Sunny \U00002600",
        "Clouds": "Cloudy \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U00002614",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
#        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"\U00002601{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\U00002601\n"
              f"Weather in the city: {city}\nTemperature: {cur_weather}C°{wd}\n"
              f"Humidity: {humidity}%\nPressure: {pressure} m.of.m\nWind: {wind} m/s\n"
              f"Sunrise:{sunrise_timestamp}\nSunset: {sunset_timestamp}\nDaylight length:{length_of_the_day}\n"
              f"Have a nice day!")

    except Exception as ex:
        print(ex)
        print("Check the name of the city")

def main():
    city = input("Input the city: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()