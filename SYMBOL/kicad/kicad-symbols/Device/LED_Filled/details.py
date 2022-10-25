
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "LED_Filled"
    hexID = "SZKDEVICELFILL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LED_Filled', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'Light emitting diode, filled shape', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('Device : LED_Filled')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

