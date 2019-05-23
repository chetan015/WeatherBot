from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import *
# https://pypi.org/project/weather-api/
from weather import Weather, Unit


class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain):
        # weather = Weather(unit=Unit.CELSIUS)
        # gpe = ('Auckland', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        # result = weather.lookup_by_location(gpe)
        # if result:
        #     condition = result.condition
        #     city = result.location.city
        #     country = result.location.country
        #     dispatcher.utter_message('It\'s ' + condition.text + ' and ' + condition.temp + '°C in ' +
        #                              city + ', ' + country + '.')
        # else:
        #     dispatcher.utter_message('We did not find any weather information for ' + gpe + '. Search by a city name.')
        #dispatcher.utter_message('Its quite hot')
        from apixu.client import ApixuClient
        api_key = '0191841c0d7a4a91b81115516191404'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('GPE')
        current = client.current(q=loc)
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)                        
        dispatcher.utter_message(response)
        return