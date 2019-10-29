# forecast-gen
A simple python system to generate products similar to NOAA Weather Radio and others.

# How to use

Edit the variables listed under the `setup` comment in `start_system.py`.

(Forecast zones & observation stations can be found here: https://api.weather.gov/offices/your_office_here)

Once those are all set up, simply run `start_system.py` in python. This will generate a fully-formatted text product in `speech.txt`.

If needed, you can edit some of the functions in `main.py` to suit what you want to output into the file in terms of formatting.

# TTS Setup
Any forecast-gen version starting from 0.2.0 supports TTS functionality.

### Software
Forecast-gen uses a software called [Balcon](http://cross-plus-a.com/balabolka.htm) to read off the text file generated from running `start_system.py`. As for voices, any SAPI 5 voice should work perfectly fine with the software above. If you're looking for a voice to start off with, you could try the voices from the [MS TTS Pack](https://archive.org/details/Sam_mike_and_mary), or i

### Running SAPI 5 voices through [WINE](https://www.winehq.org/) (Linux, macOS)

`Note: Most of these instructions are for Linux, as I don't use macOS`

Under the assumption that you have already installed WINE and winetricks through your package manager of choice, create a [32-bit wineprefix](https://wiki.winehq.org/FAQ#How_do_I_create_a_32_bit_wineprefix_on_a_64_bit_system.3F) so you can run Balcon, and then run `winetrick speechsdk` in your terminal. Once those are done, run `wine balcon -l` in the directory where Balcon is in, and it should list off some voices, by default `speechsdk` installs Microsoft Sam, Mike, and Mary.


# Notes

The software for TTS support on Linux, as well as the software for using the voices in a Linux terminal, will not work on ARM operating systems such as [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) or [Arch Linux ARM](https://archlinuxarm.org/).

