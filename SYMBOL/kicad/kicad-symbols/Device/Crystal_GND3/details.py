
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Crystal_GND3"
    hexID = "SZKDEVICEXGND3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Y', 'kicadSymbolValue': 'Crystal_GND3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'quartz ceramic resonator oscillator', 'kicadSymbolki_description': 'Three pin crystal, GND on pin 3', 'kicadSymbolki_fp_filters': 'Crystal*'}])
    newPart['name'].append('Device : Crystal_GND3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

