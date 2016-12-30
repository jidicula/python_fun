import urllib2
from bs4 import BeautifulSoup

# This script gets current conditions for any Canadian city from the Environment Canada website.

def current_weather():
    # Replace link with any city weather link from http://weather.gc.ca/
    url = urllib2.urlopen("http://weather.gc.ca/city/pages/qc-147_metric_e.html")
    soup = BeautifulSoup(url, "html.parser")
    # Get date
    observed_label = soup.find("dt",string="Date: ")
    observed = observed_label.find_next_sibling().get_text().rstrip()
    # Get temperature
    temperature_label = soup.find("dt",string="Temperature:")
    temperature = temperature_label.find_next_sibling().get_text().strip()
    # Get condition
    condition_label = soup.find("dt",string="Condition:")
    condition = condition_label.find_next_sibling().get_text().strip()
    # Get pressure
    pressure_label = soup.find("dt",string="Pressure:")
    pressure = pressure_label.find_next_sibling().get_text().strip()
    # Get tendency
    tendency_label = soup.find("dt",string="Tendency:")
    tendency = tendency_label.find_next_sibling().get_text().strip()
    # Get wind
    wind_label = soup.find("dt",string="Wind:")
    wind = wind_label.find_next_sibling().get_text().strip()
    windchill = u"N/A"
    try:
        # Get windchill, only if it can be found.
        windchill_label = soup.find("a",string="Wind Chill")
        windchill = windchill_label.find_next().get_text().strip() + u"\xb0C"
    except:
        pass

    weather_now = u"Conditions observed at: *%s*.\nTemperature: *%s*\nCondition: *%s*\nPressure: *%s*\nTendency: *%s*\nWind speed: *%s*\nWind chill: *%s*" % (observed,temperature,condition,pressure,tendency,wind,windchill)
    return weather_now

print("Weather in Montréal:")
print(current_weather())
