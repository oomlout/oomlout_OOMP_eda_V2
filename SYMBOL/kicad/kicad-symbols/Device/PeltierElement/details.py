
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "PeltierElement"
    hexID = "SZKDEVICEPELTIERELEMENT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PE', 'kicadSymbolValue': 'PeltierElement', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Peltier TEC', 'kicadSymbolki_description': 'Peltier element, thermoelectric cooler'}])
    newPart['name'].append('Device : PeltierElement')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

