import os
import main
from time import strftime, gmtime

# Setup

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

nws_office = 'VEF'      # Las Vegas National Weather Service
generateMarineForecast = False

print("Generating speech.txt...")

speech = open('speech.txt', "w+")

speech.write("FORECAST-GEN 0.0.1 - GENERATED AT " + strftime('%m/%d/%y %H:%M') + '\n')
speech.write("======================================\n")
speech.writelines("You are listening to NOAA Weather Radio Station KXI83, the voice of the National Weather Service.\n"
                + "This station originates from a transmitter located in Fort Mohave, Arizona, and data originates from the National Weather Service in Las Vegas, Nevada...\n"
                + f"The current time is {strftime('%I:%M %p %Z')}.\n"
                + "======================================\n")

speech.writelines(main.getZoneForecast(zone) for zone in zones)
speech.writelines(main.getCurrentObservations(station) for station in stations)
speech.write("======================================\n")
speech.write("The following is an Area Forecast Discussion issued by the National Weather Service...\n")
speech.writelines(main.getAFD(nws_office))
speech.write("======================================\n")


speech.close

print("Finished generating script!")