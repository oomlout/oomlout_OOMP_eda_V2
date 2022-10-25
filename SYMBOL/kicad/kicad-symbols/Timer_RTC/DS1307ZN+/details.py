
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "DS1307ZN+"
    hexID = "SZKTIMERRTCDS137ZN+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DS1307Z+', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1307ZN+', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1307.pdf', 'kicadSymbolki_keywords': 'RTC, I2C Timekeeping Chip', 'kicadSymbolki_description': '64 x 8, Serial, I2C Real-time clock, 4.5V to 5.5V VCC, -40°C to +85°C, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm?P1.27mm*'}])
    newPart['name'].append('Timer_RTC : DS1307ZN+')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

