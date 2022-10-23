
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP41100"
    hexID = "SZKPOTENTIOMETERDIGITALMCP411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP41010', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP41100', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11195c.pdf', 'kicadSymbolki_keywords': 'R POT', 'kicadSymbolki_description': 'Single Digital Potentiometer, SPI interface, 256 taps, 100 kohm', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*P1.27mm*'}])
    newPart['name'].append('MCP41100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

