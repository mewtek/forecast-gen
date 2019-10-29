import os
import json
import requests
import datetime
import math
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


# TODO: Remove redundant code & clean up a bit.

def getAlertHeadline(zone):      # Get alert headlines from a zone
    zone_alerts_url = f'https://api.weather.gov/alerts/active/zone/{zone}'
    data = requests.get(zone_alerts_url).json()

    headline = ""

    try:
        headline = data['features'][0]['properties']['parameters']['NWSheadline'][0] + "...\n"
        return headline

    except TypeError: pass
    except IndexError: pass

def getAlertName(zone):
    zone_alerts_url = f'https://api.weather.gov/alerts/active/zone/{zone}'
    data = requests.get(zone_alerts_url).json()

    alertname = ""

    try:
        alertname = data['features'][0]['properties']['event']
        return alertname
    except TypeError: return None
    except IndexError: return None


def getAlert(zone):     # Grab a full Alert product from a zone
    zone_alerts_url = f'https://api.weather.gov/alerts/active/zone/{zone}'
    data = requests.get(zone_alerts_url).json()

    alert = ""

    try:
        alert += data['features'][0]['properties']['parameters']['NWSheadline'][0] + "...\n"
        alert += data['features'][0]['properties']['description'] + "\n"
        alert += data['features'][0]['properties']['instruction'] + "\n"
        return alert
    
    except TypeError: return None
    except IndexError: return None


def getCurrentObservations(station):    # Get current observations from an observation station
    obs_url = f'https://api.weather.gov/stations/{station}/observations/latest'
    station_url = f'https://api.weather.gov/stations/{station}'
    data = requests.get(obs_url).json()
    data1 = requests.get(station_url).json()

    # These are all zero by default
    temp_c_to_f = 0
    dew_c_to_f = 0
    temp = "not available"
    dewpnt = 0
    humidity = 0
    windSpd = 0
    con = data['properties']['textDescription']
    station_name = data1['properties']['name']

    if data['properties']['dewpoint']['value'] is not None:
        dew_c_to_f = data['properties']['dewpoint']['value'] * 9 / 5 + 32
        dewpnt = str(math.floor(float(dew_c_to_f)))
    else:
        dew_c_to_f = 0
        dewpnt = 0

    if data['properties']['relativeHumidity']['value'] is not None:
        humidity = str(math.floor(float(data['properties']['relativeHumidity']['value'])))
    else:
        humidity = humidity

    if data['properties']['windSpeed']['value'] is not None:
        windSpd = str(math.floor(float(data['properties']['windSpeed']['value'])))
    else:
        windSpd = windSpd

    if data['properties']['temperature']['value'] is not None:
        temp_c_to_f = data['properties']['temperature']['value'] * 9 / 5 + 32
        temp = str(math.floor(float(temp_c_to_f))) + " degrees"
    else:
        temp_c_to_f = temp_c_to_f
        temp = "not available"

    current_conditions = ""

    try:
        if temp == "not available" and dewpnt is 0 and humidity is 0:
            current_conditions = f"The conditions at {station_name} were unavailable...\n"
            return current_conditions
        else:
            # Do this to prevent unnecessary data output
            if int(windSpd) >= 5:
                current_conditions = f"At {station_name}, it was {con}... The temperature was {temp}, the dewpoint {dewpnt}, and the relative humidity was {humidity}%... The wind was {windSpd} MPH...\n"
            else:
                current_conditions = f"At {station_name}, it was {con}... The temperature was {temp}, the dewpoint {dewpnt}, and the relative humidity was {humidity}%... \n"

            return current_conditions

    except TypeError:
        current_conditions = f"The conditions at {station_name} were unavailable...\n"
        return current_conditions
    except IndexError:
        current_conditions = f"The conditions at {station_name} were unavailable...\n"
        return current_conditions


def getZoneForecast(zone):      # Get a list of zone forecast products.
    zone_forecast_url = f'https://api.weather.gov/zones/forecast/{zone}/forecast'
    zone_url = f'https://api.weather.gov/zones/forecast/{zone}'
    data = requests.get(zone_forecast_url).json()
    data1 = requests.get(zone_url).json()

    alertHeadline = None
    zone_name = data1['properties']['name']
    zone_forecast = """"""

    if getAlertHeadline(zone) is not None:
        alertHeadline = getAlertHeadline(zone)

    try:
        
        zone_forecast += f"""The zone forecast for {zone_name}... \n"""

        if alertHeadline is not None:
            zone_forecast += f"{alertHeadline}\n"

        for i in range(0, 6):   # Zone forecast usually has 6 products
            zone_forecast += f"""{data['periods'][i]['name']}... {data['periods'][i]['detailedForecast']}\n"""

        zone_forecast += """======================================\n"""
        return zone_forecast

    except TypeError:
        zone_forecast += f"""The zone forecast for {zone_name} was unavailable...\n======================================\n"""
        return zone_forecast

    except IndexError:
        zone_forecast += f"""The zone forecast for {zone_name} was unavailable...\n======================================\n"""
        return zone_forecast

def getAFD(office):     # Scrape for an office's latest AFD product
    url = f'https://forecast.weather.gov/product.php?site={office}&issuedby={office}&product=AFD&format=TXT&version=1&glossary=0'
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    afd = soup.pre.get_text()

    return afd