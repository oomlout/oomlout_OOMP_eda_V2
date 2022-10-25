
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP41050"
    hexID = "SZKPOTENTIOMETERDIGITALMCP415"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP41010', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP41050', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11195c.pdf', 'kicadSymbolki_keywords': 'R POT', 'kicadSymbolki_description': 'Single Digital Potentiometer, SPI interface, 256 taps, 50 kohm', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*P1.27mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP41050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

