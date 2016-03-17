#! python3
# Mapit.py program - Launches a map in the browser using an address from the command line or clipboard

import webbrowser   # Launch a web browser
import sys          # Read command line arguments
import pyperclip    # Reads the contents of the clipboard

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:]) # If this evaluates to an int >1 then a command line was given
                                    # Join method will return a single string value
                                    # [1:] chops off 1st elem of array, we dont want the program name in this string
                                    # It's stored in the address variable
# TODO: Get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://maps.google.com/maps/place/1100+Meredith+Ln_plano_texas/')

