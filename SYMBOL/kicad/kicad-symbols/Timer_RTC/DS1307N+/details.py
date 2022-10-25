
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "DS1307N+"
    hexID = "SZKTIMERRTCDS137N+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DS1307+', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1307N+', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1307.pdf', 'kicadSymbolki_keywords': 'RTC, Trickle-Charge Timekeeping Chip', 'kicadSymbolki_description': '64 x 8, Serial, I2C Real-time clock, 4.5V to 5.5V VCC, -40°C to +85°C, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Timer_RTC : DS1307N+')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

