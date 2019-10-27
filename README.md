# forecast-gen
A simple python system to generate products similar to NOAA Weather Radio and others.

# How to use

Edit the variables listed under the `setup` comment in `start_system.py`.

(Forecast zones & observation stations can be found here: https://api.weather.gov/offices/your_office_here)

Once those are all set up, simply run `start_system.py` in python. This will generate a fully-formatted text product in `speech.txt`.

If needed, you can edit some of the functions in `main.py` to suit what you want to output into the file in terms of formatting.


# Notes

While there are plans of adding support for SAPI 5 TTS voices into the system, the software for the voices, as well as the software for using the voices in the console, will not work on ARM systems such as [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) or [Arch Linux ARM](https://archlinuxarm.org/) due to x86 software support being virtually nonexistant.

As for the software necessary for the TTS support to work, those will not be included in the github repo for the reason that the license for the software [balcon](http://cross-plus-a.com/balabolka.htm) is unclear. As for the voices, I'll eventually make a pack of the voices that could be used with the system, though any standard SAPI 5 voices should work just fine.
