
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_TRIAC_A1A2G"
    hexID = "SZKDEVICEQTRIACA1A2G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Q_TRIAC_A1A2G', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'TRIAC', 'kicadSymbolki_description': 'Triode for alternating current, anode1/anode2/gate'}])
    newPart['name'].append('Device : Q_TRIAC_A1A2G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

