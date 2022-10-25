
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "LED_GBKR"
    hexID = "SZKDEVICELGBKR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LED_GBKR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'LED RGB diode', 'kicadSymbolki_description': 'RGB LED, green/blue/cathode/red', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('Device : LED_GBKR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

