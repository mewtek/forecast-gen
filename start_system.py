""" FORECAST-GEN VERSION 0.1.0
This system has no afilliation with NOAA's National Weather Service, nor their CRS (Console Replacement system)
Or BMH (Broadcast Message Handler) systems. """


import os
import main
from time import strftime, gmtime

# Setup


# The zones & stations that are taken care of by your NWS forecast office can be found here:
# https://api.weather.gov/offices/your_office_id

zones = [
    'AZZ003',    # Kingman & Northwest Deserts
    'AZZ002',   # Lake Havasu, Fort Mohave
    'CAZ527',    # San Bernardino County, Upper Colorado Valley
    'NVZ021',    # Lake Mead National Recreation Area
    'NVZ020'   # Las Vegas Valley
]


stations = [    # Observation Stations
    'KIFP',    # Laughlin/Bullhead City Int. Airport
    'KIGM',     # Kingman Int. Airport
    'KLAS',      # McCarran Int. Airport
    'KLSV'      # Nellis Air Force Base
]

priority_zones = ['AZZ003', 'NVZ021']    # These should probably be the zones closest to you

nws_office = 'VEF'      # Las Vegas National Weather Service
generateMarineForecast = False      # Generate Marine Forecasts?
printScriptOnFinish = False     # Print the script to console when it's finished generating?


print("Generating speech.txt...")

speech = open('speech.txt', "w+")

speech.write("FORECAST-GEN 1.0.0 - GENERATED AT " + strftime('%m/%d/%y %H:%M') + '\n======================================\n')
speech.writelines("You are listening to NOAA Weather Radio Station KXI83, the voice of the National Weather Service.\n"
                + "This station originates from a transmitter located in Fort Mohave, Arizona, and data originates from the National Weather Service in Las Vegas, Nevada...\n"
                + f"The current time is {strftime('%I:%M %p %Z')}.\n"
                + "======================================\n")
for zone in priority_zones:
    if main.getAlert(zone) is not None:
        speech.write(f"The following is a {main.getAlertName(zone)} issued by the National Weather Service...\n")
        speech.writelines(main.getAlert(zone))
        speech.write("======================================\n")
speech.write(f"Here are the observations for the local area, as of {strftime('%I %p %Z')}...\n")
speech.writelines(main.getCurrentObservations(station) for station in stations)
speech.write("======================================\n")
speech.writelines(main.getZoneForecast(zone) for zone in zones)
speech.write("The following is an Area Forecast Discussion issued by the National Weather Service...\n")
speech.writelines(main.getAFD(nws_office))
speech.write("======================================\n")


speech.close

print("Finished generating script!")

if printScriptOnFinish is True:
    speech = open('speech.txt', 'r+')
    print(speech.read())
    speech.close
