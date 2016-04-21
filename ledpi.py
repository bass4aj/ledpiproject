from flask import Flask,request, url_for, json, Response, jsonify
from xml.parsers import expat
import RPi.GPIO as GPIO

#implement Flask 
app = Flask(__name__)

#initialize LEDS on respective pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
yellow =  GPIO.PWM(29, 50)
green =  GPIO.PWM(31, 50)
blue =  GPIO.PWM(33, 50)
yellow.start(0)
green.start(0)
blue.start(0)

#set the URL for calling the method to IP address/rest
@app.route('/rest', methods=['POST'])
def api_message():
    #handle JSON
    if request.headers['Content-Type'] == 'application/json':

        #get JSON string
        jsonRes = request.data

        #load into a dictionary
        jsonVars = json.loads(jsonRes)

        #set variables
        color = jsonVars.get('color')
        level = jsonVars.get('brightness')
        
        #use color and brightness to adjust LEDs
        if color == "blue":
            
            blue.ChangeDutyCycle(float(level))
            
        elif color == "green":
           
            green.ChangeDutyCycle(float(level))
           
        elif color == "yellow":
            yellow.ChangeDutyCycle(float(level))
    
        return "200"

    #handle XML
    elif request.headers['Content-Type'] == 'application/xml':

        #implement code to parse XML data (perhaps with ElementTree API).
        #code below was an attempt to use Python's xml.parsers.expat
        """
        xmlDict = {}
        def elementHandler(name, attr):
            if name == 'color' or name == 'brightness':
                xmlDict[name] = attr
            
        xmlRes=request.data
    
        parser=expat.ParserCreate()
        parser.StartElementHandler = elementHandler
        parser.Parse(xmlRes)
        """
        #color = xmlDict.get('color')
        #level = xmlDict.get('brightness')

        #use color and brightness to adjust LEDs
        if color == "blue":
            
            blue.ChangeDutyCycle(float(level))
           
        elif color == "green":
           
            green.ChangeDutyCycle(float(level))
            
        elif color == "yellow":
            yellow.ChangeDutyCycle(float(level))

        return "200"
    
    elif request.headers['Content-Type'] == 'application/yaml':

        #implement code to parse YAML data.


        #use color and brightness to adjust LEDs
        #color = xmlDict.get('color')
        #level = xmlDict.get('brightness')
           
        if color == "blue":
            
            blue.ChangeDutyCycle(float(level))
           
        elif color == "green":
           
            green.ChangeDutyCycle(float(level))
            
        elif color == "yellow":
            yellow.ChangeDutyCycle(float(level))
        return "200"
    else:
        return "400"
    

#initialize server on port 80
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
