Abstract
========
  
Our program allows us to use a remote device to adjust the individual 
brightness of multiple LEDs via CURL POST requests. These requests must
provide a color for the LED (yellow, green, or blue), and a brightness level 
between 0 and 100. Our program currently only supports JSON, but should 
eventually also support XML and YAML.
   
  
Environment
============
  
Our code uses the following tools:
	
	*Python 3.5
	*Raspberry Pi 3
	*Flask API version 0.10.x
	*HTML 5
  
Compilation
===========
  
To properly set up our project with the HTML pages (no longer functional),
ensure that a folder called "templates" is in the same directory as the python
script. The HTML files must be placed in that folder. Otherwise, no special organization
is required.
  

Instructions
============
  
To run the project (assuming all hardware is already assembled):
	
	1. Load the python script onto the Raspberry Pi
	2. In the terminal, navigate to the directory of the python script
	3. Enter "sudo python ledpi.py" into the terminal to start the server
	4. On another device on the same local network as the Raspberry Pi, direct CURL request to the IP address of the Raspberry Pi
