
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "CAP1206-x-SL"
    hexID = "SZKSENTOUCHCAP126XSL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAP1206-x-SL', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00001567B.pdf', 'kicadSymbolki_keywords': '6 Channel Capacitive Touch Sensor', 'kicadSymbolki_description': '6-Channel Capacitive Touch Sensor, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC?14*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Touch : CAP1206-x-SL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

